'''Every time you load this, run [pip install -U discord.py], then [python3 main.py]'''




#import discord

#class MyClient(discord.Client):
#  async def on_ready(self):
#    print('Simply fabulous! The great {0} is here!'.format(self.user))

#  async def on_message(self, message):
#    print('Message from {0.author}: {0.content}'.format(message))

#client = MyClient()
#client.run('NzAwMzk4OTY5NTQ4OTYzOTQ0.Xpia0Q.z8d82kjL-s-DYcssM2z8Lokn8Ao')

import discord

client = discord.Client()
token = 'NzAwMzk4OTY5NTQ4OTYzOTQ0.Xpia0Q.z8d82kjL-s-DYcssM2z8Lokn8Ao'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name="w!help")
    await client.change_presence(status=discord.Status.dnd, activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('w!help'):
        await message.channel.send("Hmph. So here you are, begging for my assistance. Luckily for you, I'm a benevolent deity, so I'll give you a hand... but this doesn't mean you'll get free autographs. "'\n \n'"`w!help` will prompt me to say this again. It's a huge waste of time for an idol like me, so you should probably pin this message, or whatever."'\n \n'"`w!hello` will just call me to you. Abuse this, and I'll smite you with Poison Sting the minute I track your IP.")
    if message.content.startswith('w!hello'):
        await message.channel.send('What do you want from me now?!')
    elif 'WINNIE' in message.content or 'wINNIE' in message.content:
        await message.channel.send('The heck are you yelling for?!')
    elif 'winnie' in message.content or 'Winnie' in message.content:
        await message.channel.send('You called me?')

client.run(token)