# -*- coding: utf-8 -*-
#Codado Por Kleidimar Martins - Dryrtan d(-_-)b
import os
import glob
import telegram
from telegram import ReplyKeyboardMarkup

TOKEN = '--->SEU TOKEN AQUI<---'
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
        bot.send_audio(chat_id=chat_id, audio=open('./' + musica, 'rb'), timeout=1000)
        aw = aw +1
    else:
        os.system('rm -rf *.mp3')

def sms(chat_id, sms):
    bot.send_message(chat_id=chat_id, text=sms)

def sms2(chat_id, sms):
    menu_keyboard = [['Sim'], ['Não']]
    menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
    bot.send_message(chat_id=chat_id, text=sms, reply_markup = menu_markup)
#sms(864397332, 'Teste')