import requests
import time
import json
import os
import glob
import sys
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telegram
import pathlib
import upload

class TelegramBot:

    def __init__(self):
        token = 'TOKEN AQUI'
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
                    mensagem = str(dado['message']['text'])
                    name_user = str(dado["message"]["from"]["first_name"])
                    self.name_user = name_user
                    chat_id = dado["message"]["from"]["id"]
                    self.ids = chat_id
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
    # Obtem mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=1000'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Manda musica para o bot
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        loc_txt = '/home/dryrtan/Documentos/Spotify_bot/musicas.txt'

    # Responde de acordo com o que ouver no campo 'text' da menssagem de retorno do telegram
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f''''''
        if mensagem == '/start':
            return f'Olá ' + self.name_user + ', sou um Bot de download de musicas e playlist do Spotify, manda o link e o resto deixa comigo 😊'
        
        elif 'track' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musica, agorinha enviamos.')
            os.system('spotdl --song ' + mensagem)
            return f'''Quer receber as musicas agora?{os.linesep}/sim                      /nao'''
        
        elif 'album' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musica, agorinha enviamos.')
            os.system('spotdl --album ' + mensagem + ' --write-to=' + loc_txt + ' && spotdl --list=musicas.txt && rm -rf musicas.txt')
            return f'''Quer receber as musicas agora?{os.linesep}/sim                      /nao'''
        
        elif 'playlist' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musica, agorinha enviamos.')
            os.system('spotdl --playlist ' + mensagem + ' --write-to=' + loc_txt + ' && spotdl --list=musicas.txt && rm -rf musicas.txt')
            return f'''Quer receber as musicas agora?{os.linesep}/sim                      /nao'''

        elif 'artist' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musica, agorinha enviamos.')
            os.system('spotdl --all-albums ' + mensagem + ' --write-to=' + loc_txt + '  && spotdl --list=musicas.txt && rm -rf musicas.txt')
            return f'''Quer receber as musicas agora?{os.linesep}/sim                      /nao'''

        elif 'episode' in mensagem:
            return f'''Eita, infelismente não posso fazer download de podcasts, desculpe, que tal uma música em?! '''

        elif mensagem.lower() in ('s', 'sim', '/sim'):
            upload.down(self.ids)
            return f'''Todas as sua musicas foram enviadas 😊'''
        elif mensagem.lower() in ('n', 'nao', '/nao'):
            return f'''Como quiser, mas se não poder baixar agora pode ser que aconteça alguns bugs. 😬'''
        else:
            print(mensagem)
            return f'''Humm... acho melhor você da uma olhadinha nesse link, não consegui entender. 🤔 🤷🏻‍♂️'''


    # Responde em texto
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)

Bot = TelegramBot()
Bot.Iniciar()