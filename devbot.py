import discord

TOKEN = 'NTU3ODYwNDA4NDgwODkwODkx.D3O1aw.DpwpBdlbEcC2RVMRfEplyR2pHgg'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello THERE {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!weed'):
        msg = 'My favourite thing.'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('Doc'):
        msg = 'McSexy'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
