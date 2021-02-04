import json
import os
os.system('pip install https.server')
import https.server
import socketserver
import socket
class SendVar:
  def __init__(self,directory,filename='vars.json'):
    self.dir = directory
    self.filename = filename

  def host(self,port):
    handler = https.server.SimpleHTTPRequestHandler
    os.chdir(self.dir)
    with socketserver.TCPServer(('',port), handler) as s: #serve on port
      s.serve_forever()

  def send(self,id,value):
    with open(f'{self.dir}/{self.filename}','a') as f:
      f.write(json.dumps({id:value}))
