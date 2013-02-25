#!/usr/bin/env python
#coding: utf-8
import serial
from flask import Flask, render_template,request

app = Flask(__name__)
try:
    ser = serial.Serial('/dev/ttyACM0',9600)
except:
    ser = lambda:True
    ser.write = lambda x: x

@app.route('/',methods=['POST', 'GET'])
def command():
    cmd = None
    if request.method == 'POST':
        cmd = request.form['cmd']
        ser.write(cmd)
    return render_template('cmd.html', cmd=cmd)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
