# bot.py
import logging
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

from nasa import Nasa

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
NASA_TOKEN = os.environ.get("NASA_TOKEN")

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


@bot.command(name='BEEP', help='BOOP')
async def luigi(ctx):
    await ctx.send('BOOP')


@bot.command(name='nasa', help='Astronomy Picture of the Day. Type !nasa '
                               'extra to see details ')
async def nasa(ctx, details: str = None):
    info = Nasa.get_nasa_picture(NASA_TOKEN)
    if not info:
        await ctx.send('Ocorreu um problema ao buscar a imagem do dia!')
        return

    await ctx.send(info['img'])
    await ctx.send(f"**{info['title']}**")

    if details in ['details', 'extra']:
        await ctx.send(f"{info['explanation']}")


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
