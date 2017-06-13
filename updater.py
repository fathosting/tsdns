#!/usr/bin/env python

import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    subprocess.run(["./tsdnsserver", "--update"])
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
