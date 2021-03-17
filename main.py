import discord
import os
from keep_alive import keep_alive
import yt
import to_do
import _numbers

client=discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!'):
    if message.content.startswith('!h'):
      await message.channel.send("Hello ungrateful human!")

    elif message.content.startswith('!fact'):
      _rced=_numbers.get_random_fact()     
      msg="{0} : {1}".format(_rced['num'], _rced['fact'])
      await message.channel.send(msg)

    else:
      msg= _numbers.get_num_fact(int((message.content)[1:]))
      await message.channel.send(msg)


  if message.content.startswith('$add'):
    task=message.content.split("$add ",1)[1]
    to_do.add_todo(task)
    await message.channel.send(to_do.get_tasks())

  elif message.content.startswith('$rm'):
    if "tasks" in to_do.db.keys():
      index= int(message.content.split("$rm",1)[1])
      if index>0 and (index <= len(to_do.get_tasks_list())):  
        to_do.del_todo(index-1)
        await message.channel.send(to_do.get_tasks())

      else:
        await message.channel.send('There is no task number {0}'.format(index))

  elif message.content.startswith('$todo'):
    await message.channel.send(to_do.get_tasks())

  elif message.content.startswith('$yt'):
    await message.channel.send(yt.get_subcount())
      
keep_alive()
client.run(os.getenv('TOKEN'))