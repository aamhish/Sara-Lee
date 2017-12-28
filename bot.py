# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
import os
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="lolidk", command_prefix="-", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
@client.event
async def on_message(message):
    if(message.content.find("blowtorch")!=-1):
        print('success')
        await client.send_message(message.channel, 'Blowtorches are good <3')
    

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

    await client.say(":ping_pong: Pong!")
    await asyncio.sleep(3)
@client.command()
async def sleep(lolidk):
   # await client.say(lolidk);
    await client.say(lolidk+" go to sleep before Hayley comes and finds you!!!")
    await asyncio.sleep(3)   
   
# After you have modified the code, feel free to delete the line above (line 33) so it does not keep popping up everytime you initiate the ping commmand.
    
client.run(os.environ.get('BOT_TOKEN', None))

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.
