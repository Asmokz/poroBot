import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import logging

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

#async def porofessor(ctx):
 #   await ctx.send(f"Done")


poroBot.run(os.getenv("TOKEN"), log_handler=handler, log_level=logging.INFO)

