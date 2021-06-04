import discord, chalk
from discord.ext import commands
channel_which_you_want_to_spy_on = #put the channel id here DO NOT USE INVERTED COMMA'S 
channel_which_the_messages_will_be_sent_on = #put the channel id here DO NOT USE INVERTED COMMA'S 



bot = commands.Bot(command_prefix = "|")
@bot.event
async def on_ready():
	print('The bot is online')



@bot.event
async def on_message(message):
	if message.channel.id == channel_which_you_want_to_spy_on :
		cmd = message.content
		channel = bot.get_channel(channel_which_the_messages_will_be_sent_on)
		print(cmd)
		msg = message.author
		await channel.send(f'{message.author} : {cmd}')



bot.run('TOKEN GOES HERE')
