# -*- coding: utf-8 -*-
VERSION = "graspcrx v12.5.21"
import sae
import urllib2 as urilib
from bottle import Bottle, request ,template

app = Bottle()

@app.route('/')
def index():
    return template('index.tpl')

@app.route('/crx', method='POST')
def crx():
    URI = request.forms.get('URI')
    UUID = URI.split("/")[-1]
    return template('crx',CRXUUID=UUID)

@app.route('/bookmark/:URL')
def bookmark(URL):
    print URL
    #UUID = URL[-1]
    return template('crx',CRXUUID=URL)

application = sae.create_wsgi_app(app)
#from sae.ext.shell import ShellMiddleware
#application = sae.create_wsgi_app(ShellMiddleware(app, '1q2w3e4r5t')) 
