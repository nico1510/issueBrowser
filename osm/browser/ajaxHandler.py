#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras
import sys
import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import json

PORT = 8080
appendix = {}

class ComplexEncoder(json.JSONEncoder):
  def default(self, obj):
    if hasattr(obj, 'isoformat'):
      return obj.isoformat()
    return json.JSONEncoder.default(self, obj)

class AjaxHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):  
  print """The ajax handler is running..."""
  def __init__(self, request, client_address, server):
    """ open a connection to postgres """
    try:     
      self.con = psycopg2.connect(database='postgres', user='postgres')
    except psycopg2.DatabaseError, e:
      print 'Error %s' % e  
      sys.exit(1)
    SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)

  def do_POST(self):    
    """Handle a post request"""
    length = int(self.headers.getheader('content-length'))    
    dataString = self.rfile.read(length)

    box, cats = self.decodeDataString(dataString)
    


    #cur = self.con.cursor()
    cur = self.con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    inBoundingBox = "melding_position <@ box(point '(" + box[0] + "," + box[1] + ")', point '(" + box[2] + "," + box[3] + ")')"
    sqlMeldings = "select melding_id, melding_position, hoofdcategorie_code, melding_created, melding_omschrijving, melding_datumtijd, bijlage_id  from melding where "+ inBoundingBox +" AND hoofdcategorie_code IN (" + ','.join(cats) + ");"
    print sqlMeldings
    cur.execute(sqlMeldings)
    resultObject = {}
    resultObject["meldings"] = cur.fetchall()

    sqlStats = "select hoofdcategorie_code, count(*) from melding where " + inBoundingBox + "group by hoofdcategorie_code"
    cur.execute(sqlStats)
    resultObject["stats"] = cur.fetchall()

    result = json.dumps(resultObject, cls=ComplexEncoder)

    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    self.wfile.write(result);
    self.wfile.close();

  def decodeDataString(self, dataString):
    """ sting looks like box=4.884796142578125%2C52.01658520822504%2C5.228118896484375%2C52.14318101273936&cats%5B%5D=11&cats%5B%5D=10 """
    params = dataString.split('&')
    box = params[0][4:].split('%2C')

    cats = [];
    for c in params[1:]:
      cats.append(c.split('=')[1])
    return box, cats

def start_server():
  """Start the server."""
  server_address = ("", PORT)
  server = BaseHTTPServer.HTTPServer(server_address, AjaxHandler)
  server.serve_forever()


if __name__ == "__main__":
  start_server()

