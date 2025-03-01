import os, random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', description="Este es mi bot ambiental", intents=intents)

@bot.event
async def on_ready():
    print(f'Ya estas listo para probar tu bot en DISCORD como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$ayuda'):
        await message.channel.send("Hola, espero te encuentres bien.")
        await message.channel.send("Soy un BOT que orienta a mejorar el MEDIO AMBIENTE")
        await message.channel.send("Ayudo a CLASIFICAR RESIDUOS")
        await message.channel.send("1 --->   niño")
        await message.channel.send("2 --->   joven")
        await message.channel.send("3 --->   adulto")
        await message.channel.send("ESCOGE un número que te identifique, por favor")
    
    elif message.content.startswith('$1'):
            await message.channel.send("Hola niño")
            photo=open('images/basura.jpg','rb')
            await message.channel.send(photo)
            await message.channel.send('https://i.pinimg.com/474x/16/35/ca/1635ca7eb33f543cd5f21b981f51e87e.jpg')
            await message.channel.send("Tienes estos algunos de estos residuos en tu casa?")
            
    elif message.content.startswith('$si'):
            await message.channel.send("OK. Entonces...")
            await message.channel.send("Primero----> en el tacho AMARILLO recicla los PAPELES")
            await message.channel.send("Segundo----> en el tacho AZUL recicla los VIDRIOS")
            await message.channel.send("Tercero----> en el tacho VERDE recicla los PRODUCTOS ORGÁNICOS")
            await message.channel.send("Cuarto----> en el tacho ROJO recicla los PLÁSTICOS")

    elif message.content.startswith('$gracias'):
            await message.channel.send("Cuídate mucho, hasta la próxima....")
            
    elif message.content.startswith('$2'):
            await message.channel.send("Hola joven")
            await message.channel.send('https://usil-blog.s3.amazonaws.com/PROD/blog/image/manejo-de-residuos-1-scaled.jpg')
            await message.channel.send("Te gustaría apoyar con la confección de contenedores de cartón?")

    elif message.content.startswith('$claro'):
            await message.channel.send("BIEN. Entonces...por Favor")

            await message.channel.send("Primero----> forra una caja de color AMARILLO que servirá para recicla los PAPELES")
            await message.channel.send("Segundo----> forra una caja de color AZUL que servirá para reciclar los VIDRIOS")
            await message.channel.send("Tercero----> forra una caja de color VERDE que servirá para reciclar los PRODUCTOS ORGÁNICOS")
            await message.channel.send("Cuarto----> forra una caja de color ROJO que servirá para reciclar los PLÁSTICOS")

    elif message.content.startswith('$listo'):
            await message.channel.send("MUCHAS GRACIAS. Cuídate mucho, hasta la próxima....")


    elif message.content.startswith('$3'):
            await message.channel.send("Hola caballero")
            await message.channel.send('https://www.urp.edu.pe/rcelimacallao/wp-content/uploads/2021/11/1-27.jpg')
            await message.channel.send("Le gustaría ayudar con la difusión de la importancia de reciclar los residuos?")

    elif message.content.startswith('$cuentame'):
            await message.channel.send("BIEN. Planifiquemos el trabajo")

            await message.channel.send("Primero----> Buscar información importante para fortalecer nuestros conceptos")
            await message.channel.send("Segundo----> Elaborar instructivos para compartir")
            await message.channel.send("Tercero----> Fomentar reuniones en el barrio con los vecinos")
            await message.channel.send("Cuarto----> Promover campañas de recilado en nuestro vecindario")

    elif message.content.startswith('$hecho'):
            await message.channel.send("BUEN TRABAJO. Cuídese mucho, hasta la próxima....")

    else:
        await message.channel.send('ELIJE UNA DE LAS SIGUIENTES OPCIONES...POR FAVOR... $1  $2  $3')

bot.run("MTMzNDI4ODkzOTIwNDQ3Njk2OQ.Ga-lO-.4DaDSCMbXhkR1Xy3RCh493aV3yM-AOlPA53JuE")