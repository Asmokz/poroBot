import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import logging
import random

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


load_dotenv(dotenv_path="config")

cusIntents = discord.Intents().all()


poroBot= commands.Bot(command_prefix="/",intents=cusIntents)
    
@poroBot.event
async def on_ready():
    print("poroBot est connecté au serveur.")
    

@poroBot.command(name="ping")
async def pong(ctx):
    await ctx.send(f"Pong! {round(poroBot.latency * 1000)}ms") 

""" @poroBot.command(name="act")
async def on_presence_update(before, after):
    if after.activity.name=="League of Legends":
        #await porofessor()
        print("Done") """

@poroBot.command(name="live")
async def status(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    response = response.replace(" ", "", 1)
    response = response.replace(" ", "%20")
    poroUrl = "https://porofessor.gg/fr/live/euw/"+response
    await ctx.send(poroUrl)


@poroBot.command(name="stat")
async def status(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    response = response.replace(" ", "", 1)
    response = response.replace(" ", "%20")
    poroUrl = "https://www.op.gg/summoners/euw/"+response
    await ctx.send(poroUrl)  


@poroBot.event
async def on_presence_update(before, after):
    if after.activity.name=="League of Legends" and before.activities==():
        #await porofessor()
        print(after.activity.detail)


################################UNTILTABLE###############################

@poroBot.command(name="gameadd")
async def status(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    response = response.replace(" ", "", 1).lower()
    print(response)
    if fileChecker(ctx, response) == True:
        gamefile = open("games.txt", "a")
        if os.path.getsize('games.txt') == 0:
            gamefile.write(response)
        else:
            gamefile.write("|"+response)
        gamefile.close()
        await ctx.send(response+" added succesfully")
    else:
        await ctx.send("Ce jeu est déjà dans la liste !")


@poroBot.command(name="gamedel")
async def status(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    response = response.replace(" ", "", 1).lower()
    gamefile = open("games.txt", "r")
    gamefilecontainer = gamefile.read()
    gcount = gamefilecontainer.count("|")
    print(gamefilecontainer)
    gamelist = gamefilecontainer.split("|")
    print(gamelist)
    del gamelist[gamelist.index(response)]
    gamefile.close()
    fileModifier(gamelist)
    await ctx.send(response+" deleted succesfully")


def fileModifier(gamelist):
    gamefile = open("games.txt", "w")
    i = 1
    gamefile.write(gamelist[0])
    print(len(gamelist))
    if len(gamelist) > 1:
        while i < len(gamelist):
            gamefile.write("|"+gamelist[i])
            i = i+1
    print(gamefile)
    gamefile.close()


@poroBot.command(name="gamelist")
async def status(ctx):
    gameret = ""
    gamefile = open("games.txt", "r")
    gamefilecontainer = gamefile.read()
    gcount = gamefilecontainer.count("|")
    print(gamefilecontainer) 
    gamelist = gamefilecontainer.split("|")
    print(gamelist)
    for elem in gamelist:
        gameret = gameret+" "+elem
    gamefile.close()
    await ctx.send("La liste des jeux enregistrés dans poroBot : "+gameret)


@poroBot.command(name="gamechoser")
async def status(ctx):
    gamechosen = ""
    gamefile = open("games.txt", "r")
    gamefilecontainer = gamefile.read()
    gcount = gamefilecontainer.count("|")
    print(gamefilecontainer) 
    gamelist = gamefilecontainer.split("|")
    print(gamelist)
    gamechosen = random.choice(gamelist)
    gamefile.close()
    await ctx.send("Les amis ! Le jeu auquel vous devez jouer est ... "+gamechosen+" !")


def fileChecker(ctx, game):
    gamefile = open("games.txt", "r")
    gamefilecontainer = gamefile.read()
    gcount = gamefilecontainer.count("|")
    print(gamefilecontainer) 
    gamelist = gamefilecontainer.split("|")
    print(gamelist)
    gamefile.close()
    if gamelist.count(game) > 0:
        return False
    else:
        return True



poroBot.run(os.getenv("TOKEN"), log_handler=handler, log_level=logging.INFO)

