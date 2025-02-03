from bottle import Bottle, request, response, static_file, template, BaseRequest
import subprocess
import os
from socket import gethostname, gethostbyname
import tempfile
import shutil
import zipfile

app = Bottle()

# Increase upload memory limit to 500MB
BaseRequest.MEMFILE_MAX = 500 * 1024 * 1024  # 500MB

def compress_pdf_file(input_file, output_file, compression_level):
    compression_settings = {
        'screen': '/screen',
        'ebook': '/ebook',
        'printer': '/printer',
        'prepress': '/prepress',
        'default': '/default'
    }
    quality = compression_settings.get(compression_level, '/default')
    try:
        subprocess.run([
            'gs', '-q', '-dBATCH', '-dNOPAUSE', '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.5', '-dColorConversionStrategy=/LeaveColorUnchanged',
            f'-dPDFSETTINGS={quality}', '-dEmbedAllFonts=true', '-dSubsetFonts=true',
            '-dAutoRotatePages=/None', '-dColorImageDownsampleType=/Bicubic',
            '-dGrayImageDownsampleType=/Bicubic', '-dMonoImageDownsampleType=/Subsample',
            '-dGrayImageResolution=72', '-dColorImageResolution=72', '-dMonoImageResolution=72',
            '-sOutputFile=' + output_file, input_file
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error compressing PDF: {str(e)}")

@app.route('/', method='GET')
def index():
    return template('index.html')

@app.route('/', method='POST')
def compress_pdfs():
    files = request.files.getall('file')
    compression_level = request.forms.get('compression-level')
    
    if not files or not compression_level:
        return "No files uploaded or compression level missing.", 400
    
    temp_dir = tempfile.mkdtemp()
    zip_filename = os.path.join(temp_dir, "compressed_pdfs.zip")

    try:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files:
                filename = file.filename
                input_path = os.path.join(temp_dir, filename)
                with open(input_path, 'wb') as f:
                    f.write(file.file.read())

                output_filename = f"{os.path.splitext(filename)[0]}_compressed.pdf"
                output_path = os.path.join(temp_dir, output_filename)
                compress_pdf_file(input_path, output_path, compression_level)
                zipf.write(output_path, output_filename)

        response.headers['Content-Disposition'] = f'attachment; filename="compressed_pdfs.zip"'
        return static_file("compressed_pdfs.zip", root=temp_dir, download="compressed_pdfs.zip")
    
    finally:
        shutil.rmtree(temp_dir)

if __name__ == '__main__':
    hostname = gethostname()
    local_ip = gethostbyname(hostname)
    print(f" * Running on http://0.0.0.0:1234/")
    print(f" * Running on http://{local_ip}:1234/")
    app.run(host='0.0.0.0', port=1234)
