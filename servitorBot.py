# hexarchate bot, by Ursula
# jeng-zai cards and meanings from Yoon Ha Lee's list at http://clockwiki.yoonhalee.com/index.php?title=Jeng-zai

import random
import discord
from discord.ext import commands

#insert the token for your Discord app here
TOKEN = ''

# @servitor-bot (or whatever your bot is named) to send a command
bot = commands.Bot(command_prefix=commands.when_mentioned)

#test: returns "flashing lights affirmatively"

@bot.command()
async def test(ctx):
    msg = '{0.author.mention} *flashing lights affirmatively*'.format(ctx)
    await ctx.send(msg)

#number: returns a random number between 1 and the provided value, inclusive (defaults to 6)

@bot.command()
async def number(ctx, max="6"):
    num = random.randint(1, int(max))
    num_msg = '{0.author.mention} ' + str(num)
    await ctx.send(num_msg.format(ctx))

#faction: choose a random faction (hexarchate by default, add any term to get heptarchate)

@bot.command()
async def faction(ctx, archate="hexarchate"):
    faction_list = [
        'Andan', 'Nirai', 'Vidona', 'Rahal', 'Kel', 'Shuos'
    ]
    if archate!="hexarchate":
        faction_list.append('Liozh')
    name_msg = '{0.author.mention} '+random.choice(faction_list)
    await ctx.send(name_msg.format(ctx))

#jz: choose a random jeng-zai card
#jeng-zai meanings created by Yoon Ha Lee
#the keywords "meaning" or "up" will return the meaning of the upright card
#the keywords "read" or "updown" will choose an upright or inverted card randomly

@bot.command()
async def jz(ctx, reading="none"):
    # insert jeng-zai dictionary here
    card = random.choice(list(jzdict.keys()))
    card_msg = '{0.author.mention} ' + card
    if reading == "meaning" or reading == "up":
        card_msg = card_msg + ": " + jzdict[card][0]
    if reading == "read" or reading == "updown":
        rev = random.randint(0,1)
        if rev ==1:
            card_msg = card_msg + ", Reversed" 
        card_msg = card_msg + ": " + jzdict[card][rev]
    await ctx.send(card_msg.format(ctx))

bot.run(TOKEN)
