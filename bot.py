import discord
from discord.ext import commands
import random
import csv
import json

surge = True

client = commands.Bot(command_prefix ='.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()

async def WildMagic(ctx,*,character):
    result = ''
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['Users']:
            if p['user'] == character:
                roll = random.randint(1,20)
                if roll > p['WildMagic']:
                    p['WildMagic'] = p['WildMagic']+1
                    await ctx.send(f"{character} did not surge.\nYour Wild Magic is now at {p['WildMagic']}.\nYou Rolled:{roll}")
                else:
                    p['WildMagic'] = 1
                    rollTwo = random.randint(0,99)
                    counter = 0
                    file = open('Table.csv','r')
                    reader = csv.reader(file, delimiter = ',')
                    for row in reader:
                        if counter == rollTwo:
                            for value in row:
                                result = str(result) + str(row[value])
                            await ctx.send(f"You Surged!!!\nYour effect is:{result}\n Your Wild Magic has been reset to 1")
                        counter = counter+1
                    file.close()
        json_file.close()
    with open ('data.txt','w') as file:
        json.dump(data,file)
    file.close()

@client.command()
async def BarbWildMagic(ctx,*,character):
    with open('BarbData.txt') as json_file:
        data = json.load(json_file)
        for p in data['Users']:
            if p['user'] == character:
                roll = random.randint(0,7)
                file = open('BarbTable.csv','r')
                counter = 0
                reader = csv.reader(file, delimiter = ',')
                for row in reader:
                    if counter == roll:
                        await ctx.send(f"Your effect:{row[0]}")
                    counter = counter + 1
                file.close()
        json_file.close()
@client.command()
async def spam(ctx,member,*,sentance):
    counter = 0
    while counter != 1000:
        await ctx.send(f'{member} {sentance}')
        counter = counter + 1
    

client.run('NzgxOTI4NTgyMzUxNTUyNTEz.X8ExvQ.L4W6A6ZOwIQzEUhanCNsGwwF72k')
