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
import datetime
import platform
from datetime import datetime
from pytz import timezone
tba = tbapy.TBA(os.environ.get('TBA',None));
client = Bot(description="lolidk", command_prefix="-", pm_help = True)
game_on = False;
player1 = 0;
player1score = 0;
player2 = 0;
player2score = 0;
current_player = 0;
lol = {};
sleeplolidk = {};
wakeuplolidk = {};
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
@client.event
async def on_message(message):
    tz = timezone('EST')
    if(message.content.find("blowtorch")!=-1):
        print('success')
        await client.send_message(message.channel, 'Blowtorches are good <3')
    elif(message.content.find("*Aussie Aussie Aussie*")!=-1):
	    print('success')
	    await client.send_message(message.channel,'OI OI OI')
    elif(message.content.find("*Aussie*")!=-1):
	    print('success')
	    await client.send_message(message.channel,'OI');
    elif(message.content.find("Sara Lee")!=-1):
        print('Cakes taste better when expired')
        await client.send_message(message.channel,'Cakes taste better when expired');# await client.send_message(message.channel, 'OI')
    elif(message.author.id in lol):
        await client.change_nickname(message.author, lol[message.author.id])
        await client.say("Nickname was locked. Try eating some cakes in order to ublock it!")
    elif(message.author.id in sleeplolidk):
        lol1234= int(datetime.now(tz).hour)
        print (lol1234)
        print (int(sleeplolidk[message.author.id]))
        print (int(wakeuplolidk[message.author.id]))
        if(lol1234<int(sleeplolidk[message.author.id]) and lol1234>int(wakeuplolidk[message.author.id])):
             await client.send_message(message.channel,"GO TO SLEEP SMH!!!!!");

   # elif(message.author.id=='361549038958673924'):
    #    print('me send a message yay')
     #   print(message.author.id)
     #   await client.change_nickname(message.author, "Too AUSome")  
    await client.process_commands(message)
@client.async_event
async def on_member_join(member):
    await client.send_message("welcome", 'Welcome '+member.name+' to '+client.get_server.name+'!!')
async def on_member_remove(member):
    await client.send_message("welcome", 'Bye '+member.name+ ':(')
@client.command(pass_context=True)
async def set_sleeping_time(lolidk,lol,wakeup,night):
    global sleeplolidk
    sleeplolidk[lolidk.message.mentions[0].id]=night
    wakeuplolidk[lolidk.message.mentions[0].id]=wakeup
    await client.say("<@"+lolidk.message.mentions[0].id+">'s bed time has been set :smile: They will be yelled at from "+ wakeuplolidk[lolidk.message.mentions[0].id]+" to "+ sleeplolidk[lolidk.message.mentions[0].id])
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
    print ("lolidk") 
    await asyncio.sleep(3)
@client.command(pass_context=True)
async def locknickname(lolidk, arg1):
    global lol;

    await client.say("<@"+lolidk.message.mentions[0].id+">'s nick will be locked to "+arg1);
    #lolidk.message.content-=lolidk.message.mentions[0].name
    #await client.say(arg1);
   # print ("lolidk") 
    await asyncio.sleep(3)
    lol[lolidk.message.mentions[0].id]=arg1;
    print (lol)
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


