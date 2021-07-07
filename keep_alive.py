#------------------------------------------------------------------------#
#---------------------- TO keep the bot running ------------------------#
#------------------------------------------------------------------------#

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return"Hello, I am alive!"
    
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()
