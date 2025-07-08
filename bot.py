import discord
from discord.ext import commands
from modelo import get_class
#permisos
intencions = discord.Intents.default()
intencions.message_content = True
#Objeto bot
bot = commands.Bot(command_prefix='!', intents=intencions)
#activar
@bot.event
async def on_ready():
    print(f'{bot.user.name} se ha conectado a Discord')
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def recibir(ctx):
    if ctx.message.attachments:
        for img in ctx.message.attachments:
            nombre_img = img.filename
            await img.save(f"imagenes/{nombre_img}")
            resultado = get_class(
                model_path="Keras_model.h5",
                labels_path="labels.txt",
                image_path=f"imagenes/{nombre_img}"
                )
                
            
            await ctx.send(f"resultado{resultado}")
    else:
        await ctx.send("archivo no encontrado")

#correr
token = "TOKEN"
bot.run(token)
