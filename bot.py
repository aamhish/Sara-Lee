import discord
import asyncio
import json
import logging
import traceback
import os
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="lolidk", command_prefix="-", pm_help = True)


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
@client.event
async def on_message(message):
    if(message.content.find("blowtorch")!=-1):
        print('success')
        await client.send_message(message.channel, 'Blowtorches are good <3')
    elif(message.content.find("*Aussie Aussie Aussie*")!=-1):
        print('success')
        await client.send_message(message.channel, 'OI OI OI')
    elif(message.content.find("*Aussie*")!=-1):
        print('success')
        await client.send_message(message.channel, 'OI')
    await client.process_commands(message)
    

game_on = False;
player1 = 0;
player2 = 0;
current_player = 0;
@client.command()
async def ping(*args):

    await client.say(":ping_pong: Pong!")
    await asyncio.sleep(3)
@client.command()
async def sleep(lolidk):
   # await client.say(lolidk);
    await client.say(lolidk+" go to sleep before Hayley comes and finds you!!!")
    await asyncio.sleep(3)
@client.command(pass_context=True)
async def startblackjack(ctx):
   # player2=player2_
    await client.say("Welcome to Good Ol' Blackjack. <@" +ctx.message.author.id+">. Today you will be playing with <@"+ctx.message.mentions[0].id+">.");
    game_on = True;
    await client.say(lolidk + " your turn buddy Draw or Pass?"); 
client.run(os.environ.get('BOT_TOKEN', None))

