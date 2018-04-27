import discord
import asyncio
import json
import logging
import traceback
import tbapy
import os
from discord.ext.commands import Bot
from discord.ext import commands
from random import randint
import platform
tba = tbapy.TBA(os.environ.get('TBA',None));
client = Bot(description="lolidk", command_prefix="-", pm_help = True)
game_on = False;
player1 = 0;
player1score = 0;
player2 = 0;
player2score = 0;
current_player = 0;

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
    elif(message.author.id=='338163785082601473'):
        print('Hayl send a message yay')
        await client.change_nickname(338163785082601473, "Too AUSome")
    elif(message.author.id=='361549038958673924'):
        print('me send a message yay')
        print(message.author.id)
        await client.change_nickname(361549038958673924, "Too AUSome")
    await client.process_commands(message)
@client.async_event
async def on_member_join(member):
    await client.send_message("welcome", 'Welcome '+member.name+' to '+client.get_server.name+'!!')
async def on_member_remove(member):
    await client.send_message("welcome", 'Bye '+member.name+ ':(')

@client.command()
async def teamname(lolidk):
    lol = tba.team("frc"+lolidk)
    await client.say("Team "+str(lolidk)+" is called: "+lol['nickname']);
@client.command()
async def fourteen(lolidk):
     await client.say("03!");


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
async def gotosleep(ctx):
   # await client.say(lolidk);
    player2=ctx.message.mentions[0];
    await client.send_message(player2, "<@"+player2.id+">"+"go to sleep before Hayley comes and finds you!!!")
    await asyncio.sleep(3)
@client.command(pass_context=True)
async def go2sleep(ctx):
   # await client.say(lolidk);
    player2=ctx.message.mentions[0];
    await client.send_message(player2, "<@"+player2.id+">"+"go to sleep!!!")
    await asyncio.sleep(3)
@client.command(pass_context=True)
async def startblackjack(ctx):
    global game_on;global player1; global player1score; global player2; global player2score; global current_player; 
    player1score = 0;
   # player2=player2_
    await client.say("Welcome to Good Ol' Blackjack. <@" +str(ctx.message.author.id)+">. Today you will be playing with <@"+str(ctx.message.mentions[0].id)+">.");
    game_on = True;
    player1=ctx.message.author.id;
    player2=ctx.message.mentions[0].id;
    await client.say( "<@" +player1+">" + " your turn buddy Draw or Stand?");
    current_player=1;
@client.command(pass_context=True)
async def draw (ctx):
    global game_on;global player1; global player1score; global player2; global player2score; global current_player;
    #switch(current_player):
    if(current_player==1): 
        lol = player1;
    else:
        lol = player2;
    print ("player1:")   
    print(player1)
    print ("player2:") 
    print(player2)
    print ("person in command")
    print(ctx.message.author.id)
    if(ctx.message.author.id==lol):
        if(game_on):
            if(current_player==1):
                value = randint(1,10);
                player1score+=value
                await client.say( "<@" +str(player1)+">" + " has drawn a "+str(value)+". Total score right now is: "+str(player1score));
                
                print(player1score)
                if(player1score>21):
                    await client.say( "<@" +str(player2)+">" + " Your friend was busted and so you won!!");
                    stopgame();
                elif(player1score==21):
                    await client.say( "<@" +str(player1)+">" + " You have won!!");
                    stopgame()
                else:
                    await client.say( "<@" +str(player2)+">" + " your turn buddy! Draw or Stand?");
                    current_player = 2;
            else:
                value = randint(1,10);  
                player2score+=value 
                await client.say( "<@" +str(player2)+">" + "has drawn a "+str(value)+ ". Total score right now is: "+str(player2score));
                if(player2score>21):
                    await client.say( "<@" +str(player1)+">" + " Your friend was busted and so you won!!");
                    stopgame();
                    #break;
                elif(player2score==21):
                    await client.say( "<@" +str(player2)+">" + " You have won!!");   
                    stopgame(); 
                else:
                   
               
                    await client.say( "<@" +str(player1)+">" + " your turn buddy! Draw or Stand?");
                    current_player = 1;
        else:
            await client.say("Uh, there is no game going on right now. I am slightly confused as to what you are doing...")
    else:
        await client.say("Buddy. If you are going to be like this. There is no point in playing. Game is off. DO NOT play out of turn!")
        stopgame();
@client.command(pass_context=True)
async def stand (ctx):
    global game_on; global player1; global player1score; global player2; global player2score; global current_player;
    if(current_player==1): 
        lol = player1;
    else:
        lol = player2;
    
    if(ctx.message.author.id==lol):
        if(game_on):
            if(current_player==1):
                value = randint(1,10);
                await client.say( "<@" +str(player1)+">" + " has passed!");
                await client.say( "<@" +str(player2)+">" + " your turn buddy! Draw or Stand?");
                current_player = 2;
            else:
                value = randint(1,10);
                await client.say( "<@" +str(player2)+">" + " has passed!");
                await client.say( "<@" +str(player1)+">" + " your turn buddy! Draw or Stand?");
                current_player = 1;
        else:
            await client.say("Uh, there is no game going on right now. I am slightly confused as to what you are doing...")
    else:
        await client.say("Buddy. If you are going to be like this. There is no point in playing. Game is off. DO NOT play out of turn!")
        stopgame();

async def stopgame ():
    global game_on;global player1; global player1score; global player2; global player2score; global current_player;
    game_on= False;
    game_on = False;
    player1 = 0;
    player1score = 0;
    player2 = 0;
    player2score = 0;
    current_player = 0;
@client.command()
async def endgame():
    global game_on;global player1; global player1score; global player2; global player2score; global current_player;
    game_on= False;
    game_on = False;
    player1 = 0;
    player1score = 0;
    player2 = 0;
    player2score = 0;
    current_player = 0;
client.run(os.environ.get('BOT_TOKEN', None))


