import discord
import requests
from flask import Flask, request
import configuration_reader

app = Flask(__name__)

token=configuration_reader.get_config('token_discord')
if token == "ERROR":
    print("Hay un fallo con el modulo configuration_reader.py")

class MyClient(discord.Client): #Crea el "esqueleto" o "plantilla" para el codigo
    async def on_ready(self):
        print(f'Iniciado sesión como {self.user}')

    async def on_message(self, message):
        #Detecta si has usado la palabra clave Hal/hal para poder responderte
        print(f'Message de {message.author}: {message.content}')
        if message.content.startswith("Hal") or message.content.startswith("hal"):
            print("Palabra clave detectada, enviando...")
            SERVER_URL=f"http://{configuration_reader.get_config('ip_pc')}:5000/solicituddiscord"
            print(SERVER_URL)
            try:
                payload={"mensaje": message.content}
                respuesta=requests.post(SERVER_URL, json=payload, timeout=20)
                print("Recibido: 200")
                await message.channel.send(respuesta.text)
            except:
                print(f"ERROR: No se pudo enviar la respuesta (Revisa el timeout)")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

if token == 'token_discord':
    print('Porfavor, inserta un token valido en el archivo de configuracion')
else:
    try:
        client.run(token)
    except:
        print(f"token {token}")
        print('Error al validar el token')
