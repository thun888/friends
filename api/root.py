# -*- coding: UTF-8 -*-
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    return redirect('https://blog.thun888.xyz')
