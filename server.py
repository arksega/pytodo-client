#!/usr/bin/python
from bottle import request, route, run
import json

@route('/')
def get():
    return json.dumps([{'text':'Tarea 1','done':True},{'text':'Tarea 2','done':False}])

run()
# vim: sw=4 sts=4 si et
