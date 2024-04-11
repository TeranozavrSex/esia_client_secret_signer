import tempfile, base64, subprocess, os
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    if self.path[1:5] != "sign":
      self.send_response(500)
      return
    thumbprint = '' # Укажите SHA1 отпечаток сертификата, связанного с закрытым ключем.
    data = self.path[6:].replace("%20", " ")

    tmp_dir = tempfile.gettempdir()
    source_file = tempfile.NamedTemporaryFile(mode="w", delete=False, dir=tmp_dir)
    source_file.write(data)
    source_file.close()
    source_path = source_file.name
    destination_path = source_path + ".sgn"

    subprocess.run(["C:\\Program Files (x86)\\Crypto Pro\\cryptcp.win32.exe","-signf", "-norev", "-dir", str(tmp_dir), "-der", "-strict", "-cert", "-detached", "-thumbprint", str(thumbprint), str(source_path)])
    raw_client_secret = open(destination_path, "rb").read()

    self.send_response(200)
    self.end_headers()
    self.wfile.write(bytes(str(base64.urlsafe_b64encode(raw_client_secret).decode('utf-8')), 'utf8'))
    os.remove(destination_path)
    os.remove(source_path)


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
