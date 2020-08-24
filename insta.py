from sys import argv
import urllib
from bs4 import BeautifulSoup
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import autopep8


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
 def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		f = open("index.html", "r")
		self.wfile.write(bytes(f.read(), "utf8"))
		return
 def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        selta=post_data.decode('utf-8').split("=")[1]
        selta=selta.replace("%2F", "/")
        selta=selta.replace("%3A",":")
        selta=selta.replace("%3F","?")
        selta=selta.replace("%3D","=")
        print(selta)

    
 def DownloadSingleFile(fileURL):
        print ('Downloading image...')
        f = urllib.urlopen(fileURL)
        htmlSource = f.read()
        soup = BeautifulSoup(htmlSource,'html.parser ')
        metaTag = soup.find_all('meta', {'property':'og:image'})
        imgURL = metaTag[0]['content']
        fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'
        urllib.urlretrieve(imgURL, fileName)
   

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('0.0.0.0', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()