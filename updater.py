#!/usr/bin/env python3

import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import subprocess

settings_filepath = "/home/teamspeak/teamspeak3-server_linux_amd64/tsdns/tsdns_settings.ini"

class MyHandler(BaseHTTPRequestHandler):
  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    self._set_headers()

  def do_POST(self):
    urllib.request.urlretrieve(os.environ.get('MEH_MAP_URL'), settings_filepath)
    subprocess.call(["./tsdnsserver", "--update"])

    self._set_headers()
    self.wfile.write(b'OK')

if __name__ == '__main__':
  if not os.environ.get('MEH_MAP_URL'):
    sys.exit('please provide MEH_MAP_URL environement variable. Abording...')

  server_address = ('0.0.0.0', 8080)
  httpd = HTTPServer(server_address, MyHandler)

  print ('Server listening on %s:%s' % (server_address[0], server_address[1]))
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass

  httpd.server_close()
