from discord.ext import commands
import os, random
import requests
import discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command('merhaba')
async def mrb(ctx):
    await ctx.send(f"Merhaba! Çevre kirliliği ne biliyor musunuz? Wikipedia'ya göre çevre kirliliği; çevrenin doğal olmayan bir şekilde insan eliyle doğallığının bozulmasıdır. Bu ekosistemi bozma eylemleri; kirlenme şeklinde tabir edilmektedir.")

@bot.command('gorevler')
async def grv(ctx):
    await ctx.send(f"Tamamdır! İşte yapılabilecek görevler: 1.Geri dönüşüm yapmak, 2.İnsanları uyarmak, 3.Yere çöp atmamak, 4.Ağaç ekmek, 5.naylon poşet kullanmamak...")
   
@bot.command('yapildi')
async def brv(ctx):
    await ctx.send(f"Görevler tamam mı? Bravo!") 
    
bot.run("token")
