# -*- coding: utf-8 -*-
import os
import sys
import glob
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telegram
import pathlib


TOKEN = 'TOKEN AQUI'
bot = telegram.Bot(token=TOKEN)

def down(chat_id):
    lista = glob.glob('*.mp3')
    numero_de_musicas = len(lista)
    at = numero_de_musicas - 1
    aw = 0
    os.system("find -size +45M -exec rm -f {} \;") #Devido a limitação de envio de 50Mb do Telegram

    while aw <= at:
        musica = lista[aw]
        #bot.send_message(chat_id=chat_id, text='teste')
        bot.send_audio(chat_id=chat_id, audio=open('/home/dryrtan/Documentos/Spotify_bot/' + musica, 'rb'), timeout=1000)
        aw = aw +1
    else:
        os.system('rm -rf *.mp3')

def sms(chat_id, sms):
    bot.send_message(chat_id=chat_id, text=sms)
