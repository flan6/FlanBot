# bot.py
import os
import random
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

logging.basicConfig(filename='flanbot.log',
                    format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)

bot = commands.Bot(command_prefix='!')


@bot.command(name='roll-dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    logging.info(f'{ctx.author} rolled {dice}')
    await ctx.send(', '.join(dice))


@bot.command(name='BEEP', help='Mario.')
async def luigi(ctx):
    await ctx.send('BOOP')

if __name__ == '__main__':
    bot.run(TOKEN)
