import discord
import os
client = discord.Client()
ccnames = ['nerd', 'ryan', 'tom', 'cclist']
cctexts = ['Code Master', 'Probst King', 'Safari Creator', ccnames]

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
  if message.author == client.user:
    return

  global ccnames
  global cctexts

  command = message.content[len('&'):].strip()

  if message.content.startswith('&'):
    if command in ccnames:
      msg = cctexts[ccnames.index(command)]  
      await client.send_message (message.channel, msg)

    if command.startswith('addcommand'):
      ccaddvar1 = command[len('addcommand'):].strip()
      ccaddvar1_5 = ccaddvar1.split(' ', 1)[0]
      ccaddvar2 = ccaddvar1[len(ccaddvar1_5):].strip()
      ccaddvar3 = ccaddvar1.split(' ', 1)[0]
      if ccaddvar3 not in ccnames:
        ccnames.append(ccaddvar3)
        cctexts.append(ccaddvar2)
      else:
        msg = 'that command already exists!'
        await client.send_message (message.channel, msg)

    if command.startswith('delcommand') and command[len('delcommand '):].strip() in ccnames:
      delvar1 = command[len('delcommand '):].strip()
      delvar2 = ccnames.index(delvar2)
      ccnames.remove(delvar1)
      cctexts.remove(cctexts[delvar2])

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
