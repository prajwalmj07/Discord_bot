import discord


from discordcht import get_response
from train_model import ATrain

ATrain()

async def send_message (message, user_message, is_private):
    try:
        text =  user_message
        response  = get_response(text)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
            print(e)

def runbot():
  TOKEN  = '' #add bot token
  intents =  discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def onready():
    print(f'{client.user}is now running')

  @client.event
  async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username}said: {user_message}({channel})')

    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message,user_message,is_private=True)
    else:
        await send_message(message,user_message,is_private=False)

  client.run(TOKEN)




