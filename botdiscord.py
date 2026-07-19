import random, asyncio
import os
import discord
import requests
import settings
from discord.ext import commands
from settings import settings
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    imagenes = (os.listdir('img'))
    with open(f'img/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)  
    await ctx.send(file=picture)
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtract two numbers together."""
    await ctx.send(left - right)
@bot.command()
async def multiply(ctx, left: int, right: int):
    """Multiply two numbers together."""
    await ctx.send(left * right)
@bot.command()
async def split(ctx, left: int, right: int):
    """Split two numbers together."""
    await ctx.send(left / right)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def password(ctx, longitud=  int):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(longitud):
        password += random.choice(elements)

    await ctx.send("tu clave es:", password)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def deleteme(ctx):
    """Borra el mensaje del usuario y el del bot luego de unos segundos"""
    try:
        aviso = await ctx.send("Tu mensaje se borrará en 3 segundos... 🕒")
        await asyncio.sleep(3)  

        await ctx.message.delete()  
        await aviso.delete()       

    except discord.Forbidden:
        await ctx.send("No tengo permisos para borrar mensajes.")
    except Exception as e:
        await ctx.send(f"Ocurrió un error: {e}")
    
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('M2L1/img'))
    with open(f'M2L1/img/{img_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def RocketLeague(ctx):
    await ctx.send(f"""Hola, soy un bot, me llamo Hez {bot.user}!
                            """)
    await ctx.send(f'Te voy hablar un poco sobre Rocket League')
    await ctx.send(f'Rocket League es un videojuego que combina el fútbol con los vehículos. Fue desarrollado por Psyonix El juego se lanzó por primera vez para PlayStation 4 y Windows en julio de 2015, y más tarde se lanzaron ports para Xbox One y Nintendo Switch. En junio de 2016, 505 Games comenzó a distribuir una versión física minorista para PlayStation 4 y Xbox One, y Warner Bros. Interactive Entertainment se hizo cargo de esas funciones a finales de 2017; También se lanzaron versiones para macOS y Linux en 2016, pero el soporte para los servicios en línea se abandonaron en 2020. El juego pasó a ser free to play en septiembre de 2020, cuando Epic Games tomó posesión.')
    await ctx.send("Quieres consejos para mejorar en Rocket League? Responde con 'si' o 'no'.")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['Sí', 'Si', 'No', 'sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['Sí', 'Si', 'sí', 'si']:
            await ctx.send("1. Ser paciente, no siempre tienes que ir por el balon")
            await ctx.send("2. Dar espacio a los compañeros (si juegas en cooperativo)")
            await ctx.send("3. Evitar el Double Commit, es cuando dos personas en el mismo tranvía intentan golpear la pelota al mismo tiempo, sin comunicárselo y sin la intención de pellizcarla con su compañero.")
            await ctx.send("4. Pases efectivos (si juegas en cooperativo)")
            await ctx.send("5. Saber el posicionamiento del equipo, si tu compañero ataca tu lo apoyas pero vas un poquito mas atras, y viceversa si tu eres el que ataca (si juegas en cooperativo)")
            await ctx.send("6. Molestar a rivales; factor psicológico")
            await ctx.send("7. Practicar en campo de entrenamiento")
            await ctx.send("8. Practicar 1 contra 1") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
@bot.command()
async def bio(ctx, response=None):
    await ctx.send(f"Hola, soy un asistente que te ayuda con la contaminación: {bot.user}!")
    await ctx.send("Para empezar, dime qué tipo de contaminación te interesa: aire, agua, suelo o acustica.")

    def check(message):
        return (
            message.author == ctx.author and
            message.channel == ctx.channel and
            message.content.lower() in ['aire', 'agua', 'suelo', 'acustica']
        )

    try:
        response = await bot.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("No recibi respuesta a tiempo, intentalo denuevo.")
        return

    tipo = response.content.lower()
    if response:
        if tipo == 'aire':
            await ctx.send("La contaminacion del aire ocurre cuando sustancias mortales o nocivas, como partículas solidas y gases se dispersan en la atmósfera")
            await ctx.send("stas sustancias provienen principalmente de vehículos, fábricas, quema de combustibles y procesos industriales. Los efectos incluyen problemas respiratorios, enfermedades cardiovasculares y, según estudios recientes, un mayor riesgo de tumores cerebrales como los meningiomas")
            await ctx.send("https://tenor.com/view/roblox-industrialist-industrialist-players-pollution-gif-6673786930248027286")
        elif tipo == 'agua':
            await ctx.send("La contaminación del agua sucede cuando sustancias químicas, microorganismos o residuos alteran la calidad del agua, haciéndola tóxica para el consumo humano, la fauna y la flora. Las principales causas incluyen:")
            await ctx.send("Vertidos industriales y domésticos sin tratar.")
            await ctx.send("Agricultura intensiva que utiliza pesticidas y fertilizantes.")
            await ctx.send("Derrames de petróleo y productos químicos.")
            await ctx.send("https://tenor.com/view/dirty-water-the-simpsons-bart-simpson-lisa-simpson-pollution-gif-12793952")
        elif tipo == 'suelo':
            await ctx.send("La contaminación del suelo implica la alteración de sus características físicas, químicas y biológicas debido a la presencia de sustancias tóxicas.")
            await ctx.send("Las principales causas incluyen:")
            await ctx.send("Uso excesivo de pesticidas y fertilizantes en la agricultura.")
            await ctx.send("Vertidos industriales y residuos sólidos mal gestionados.")
            await ctx.send("Derrames de productos quimicos y metales pesados.")
            await ctx.send("https://tenor.com/view/smog-air-pollution-pollution-bad-air-gif-12428217")
        elif tipo == 'acustica':
            await ctx.send("La contaminación acústica se refiere a la presencia de ruidos excesivos en el ambiente, que pueden afectar la salud y el bienestar de las personas.")
            await ctx.send("Las principales fuentes incluyen:")
            await ctx.send("Tráfico vehicular y ferroviario.")
            await ctx.send("Obras de construcción y maquinaria pesada.")
            await ctx.send("Actividades industriales y comerciales.")
            await ctx.send("https://tenor.com/view/vagrant-queen-vagrants-syfy-vagrant-loud-gif-16912713")
import random

@bot.command()
async def biofact(ctx):
    await ctx.send("Aqui tienes un dato interestante sobre la contaminación")
    await ctx.send(random.choice([
        "La contaminación del aire causa aproximadamente 7 millones de muertes prematuras al año a nivel mundial.",
        "El 80 porciento e la contaminación del agua proviene de fuentes terrestres, como la agricultura y la industria.",
        "Se estima que el 30 porciento e los suelos agrícolas en el mundo están degradados debido a la contaminación y prácticas insostenibles.",
        "La contaminación acústica puede afectar la salud mental y física, aumentando el estrés y el riesgo de enfermedades cardiovasculares.",
        "El plástico representa el 80 porcfiento de la contaminación marina, afectando a la vida marina y a los ecosistemas acuáticos.",
        "El dióxido de carbono (CO2) es el principal gas de efecto invernadero, y su concentración ha aumentado un 40 porciento sde la Revolución Industrial.",
        "La contaminación del aire puede reducir la esperanza de vida en hasta 2 años en algunas regiones del mundo.",
        "El reciclaje de papel puede reducir la contaminación del agua en un 35% y la contaminación del aire en un 74% en comparación con la producción de papel nuevo.",
        "Las emisiones de vehículos son responsables de aproximadamente el 30 porciento e la contaminación del aire en las ciudades.",
        "El ruido del tráfico puede aumentar el riesgo de enfermedades cardiovasculares y problemas de sueño."
    ]))
bot.run(settings["DISCORD_BOT_TOKEN"])
