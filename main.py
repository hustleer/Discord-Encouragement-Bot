#reference:             https://www.youtube.com/watch?v=SPTfmiYiuok
Discord_developers_page:  https://discord.com/developers/applications

replit(bot_hosted_on): https://replit.com/@aries0/Encouragement-Bot#main.py
uptime_robort(to keep bot up and running): https://uptimerobot.com      #To keep the bot up and running

import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "hurt", "pain"]

starter_encouragements = [
  "Cheer up!",
  "You are a great person / bot!",
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_joke():
    response = requests.get("https://imao.herokuapp.com/jokes/api/random/")
    json_data = response.json()
    joke = str(json_data['title']) + ' : ' + str(json_data['body']) + ' - ' + str(json_data['author'])
    return(joke)

def get_jokes(no_of_jokes):
    response = requests.get("https://imao.herokuapp.com/jokes/api/{}/".format(int(no_of_jokes)))
    jokes=[]
    for joke in response.json()['jokes']:
        jokes.append(str(joke['title']) + ' : ' + str(joke['body']) + ' - ' + str(joke['author']))
    return(jokes)

def get_puns():
    return('Puns are comming soon!')

def get_riddles():
    return('Riddles are comming soon!')
    

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = list(db["encouragements"])
  #if len(encouragements) > index:
  if index in encouragements:
    #del encouragements[index]
    encouragements.remove(index)
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  elif msg.startswith('$joke'):
    if msg == '$joke':
        jokes = get_joke()
    else:
      try:
        n = int(msg.split(' ')[1].strip())
      except:
        n = int(msg.split(' ')[2].strip())
        jokes = get_jokes(n)
    await message.channel.send(jokes)
  
  elif msg.startswith('$riddle'):
    riddle = get_riddles()
    await message.channel.send(riddle)
  
  elif msg.startswith('$puns'):
    puns = get_puns()
    await message.channel.send(puns)
    
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      #print(list(db["encouragements"]))
      options = options + list(db["encouragements"])


    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
  
  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")
  
  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = msg.split("$del",1)[1]
      delete_encouragment(index)
      encouragements = list(db["encouragements"])
    await message.channel.send(encouragements)
  
  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = list(db["encouragements"])
    await message.channel.send(encouragements)
  
  if msg.startswith(".responding") or msg.startswith(".activate") or msg.startswith(".deactivate"):
    switch = msg.split("$responding ",1)[1].lower()

    if switch == "true" or switch =='t' or switch =='yes' or switch =='on':
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")


keep_alive()
client.run(os.environ['TOKEN'])
