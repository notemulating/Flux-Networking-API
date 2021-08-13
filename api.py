import flask
from pythonping import ping
from flask import render_template
import sys
from scapy import route
from scapy.all import *
import threading
import socket

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/ping/<name>', methods=['GET'])
def home(name):
    ip = str(name)
    icmp = IP(dst=ip)/ICMP()

    resp = sr1(icmp,timeout=10)
    if resp == None:
        return f"{ip} Is Down"
    else:
        return f"{ip} Is Up"



app.run()