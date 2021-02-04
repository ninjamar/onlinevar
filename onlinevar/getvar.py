import requests
import json

class GetVar:
  def __init__(self,url):
    self.url = url
  
  def get(self,var):
    req = requests.get(self.url)
    text = req.text
    try:
      return json.loads(text)[var]
    except json.decoder.JSONDecodeError:
      return 'JSONDecodeError'
