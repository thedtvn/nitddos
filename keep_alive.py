import os
import sys
import time
import random
import requests
from flask import Flask, request
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return """
a 
    """

def run():
  app.run(host='0.0.0.0',port=random.randint(1000, 9999))

def keep_alive():
    t = Thread(target=run)
    t.start()