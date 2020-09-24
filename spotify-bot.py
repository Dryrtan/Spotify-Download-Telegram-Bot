import requests
import time
import json
import os
import glob
import sys
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telegram
import pathlib

class TelegramBot:

    def __init__(self):
        token = 'SEU TOKEN AQUI'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    #Lê partes ecenciais da menssagem retorno do telegram
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"])
                    chat_id = dado["message"]["from"]["id"]
                    self.id = chat_id
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
    # Obtem mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Manda musica para o bot
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        def up():
            TOKEN = token
            bot = telegram.Bot(token=TOKEN)
            chat_id1 = self.id
            lista = glob.glob('*.mp3')
            numero_de_musicas = len(lista)
            at = numero_de_musicas - 1
            aw = 0

            while aw <= at:
                musica = lista[aw]
                bot.send_audio(chat_id=chat_id1, audio=open('/home/dryrtan/Documentos/Spotify_bot/' + musica, 'rb'))
                aw = aw +1

            else:
                os.system('rm -rf *.mp3')
    # Responde de acordo com o que ouver no campo 'text' da menssagem de retorno do telegram
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Ola, sou um Bot de download de musicas e playlist do Spotify, manda o link e o resto deixa comigo 😊'''
        if mensagem == '/start':
            return f'''Ola, sou um Bot de download de musicas e playlist do Spotify, manda o link e o resto deixa comigo 😊'''
        
        elif 'track' in mensagem:
            os.system('spotdl --song ' + mensagem)
            return f'''Terminei de sua musicas,{os.linesep}Quer receber as musicas agora?{os.linesep}/sim                      /nao'''
        
        elif 'album' in mensagem:
            os.system('spotdl --album ' + mensagem + ' --write-to=/home/dryrtan/Documentos/Spotify_bot/musicas.txt && spotdl --list=musicas.txt && rm -rf musicas.txt')
            return f'''Baixando seu album,{os.linesep}Quer receber as musicas agora?{os.linesep}/sim                      /nao'''
        
        elif 'playlist' in mensagem:
            os.system('spotdl --playlist ' + mensagem + ' --write-to=/home/dryrtan/Documentos/Spotify_bot/musicas.txt && spotdl --list=musicas.txt && rm -rf musicas.txt')
            return f'''Baixando sua playlist,{os.linesep}Quer receber as musicas agora?{os.linesep}/sim                      /nao'''

        elif 'artist' in mensagem:
            os.system('spotdl --all-albums ' + mensagem + ' --write-to=/home/dryrtan/Documentos/Spotify_bot/musicas.txt  && spotdl --list=musicas.txt && rm -rf musicas.txt')
            return f'''Baixando sua playlist,{os.linesep}Quer receber as musicas agora?{os.linesep}/sim                      /nao'''

        elif 'episode' in mensagem:
            return f'''Eita, infelismente não posso fazer download de podcasts, desculpe, que tal uma música em?! '''

        elif mensagem.lower() in ('s', 'sim', '/sim'):
            up()
        elif mensagem.lower() in ('n', 'nao', '/nao'):
            return f'''Como quiser, mas se não poder baixar agora pode ser que aconteça bugs.'''
        else:
            return f'''Humm... acho melhor você da uma olhadinha nesse link, não consegui entender. 🤔 🤷🏻‍♂️'''


    # Responde em texto
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)

Bot = TelegramBot()
Bot.Iniciar()