#!/usr/bin/env python3

import os, subprocess
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

settings_filepath = "/home/teamspeak/teamspeak3-server_linux_amd64/tsdns/tsdns_settings.ini"

class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    urllib.request.urlretrieve(os.environ.get('MEH_MAP_URL'), settings_filepath)

    subprocess.call(["./tsdnsserver", "--update"])
    self.send_response(200)
    return

if __name__ == '__main__':
  server_address = ('0.0.0.0', 8080)
  httpd = HTTPServer(server_address, MyHandler)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass

  httpd.server_close()
