#!/usr/bin/env python
#coding: utf-8
import serial
from flask import Flask, render_template,request

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0',9600)


@app.route('/',methods=['POST', 'GET'])
def msg():
    msg = None
    if request.method == 'POST':
        msg = request.form['msg']
        ser.write(msg)
    return render_template('msg.html', msg=msg)



if __name__ == "__main__":
    app.run()
