#Codado Por Kleidimar Martins - Dryrtan d(-_-)b
import requests
import json
import os
import upload
import time
import config

class TelegramBot:

    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot'+config.TOKEN+'/'

    #Lê partes ecenciais da menssagem retorno do telegram
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    try:
                        update_id = dado['update_id'] #Pega o id da mensagem
                        mensagem = str(dado["message"]["text"]) #texto da mensagem
                        name_user = str(dado["message"]["from"]["first_name"]) #nome do usuario
                        self.name_user = name_user
                        chat_id = dado["message"]["from"]["id"] #id do usuario
                        self.ids = chat_id
                        eh_primeira_mensagem = int(
                            dado["message"]["message_id"]) == 1
                        resposta = self.criar_resposta(
                            mensagem, eh_primeira_mensagem)
                        self.responder(resposta, chat_id)
                        
                    except:
                        time.sleep(5)
                        pass
    # Obtem mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=1000' #tempo de espera
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao) #requisicao
        return json.loads(resultado.content)
    
    # Manda musica para o bot
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        os.system(f'mkdir ./{config.pasta_downloads}')
    # Responde de acordo com o que ouver no campo 'text' da menssagem de retorno do telegram
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'Olá ' + self.name_user + ', sou um Bot de download de musicas e playlist do Spotify, manda o link e o resto deixa comigo 😊'
        if mensagem == '/start':
            return f'Olá ' + self.name_user + ', sou um Bot de download de musicas e playlist do Spotify, manda o link e o resto deixa comigo 😊'
        
        elif 'track' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musica, agorinha enviamos.')
            print(f'savify "{mensagem}" -q best -f mp3 -o "./{config.pasta_downloads}"')
            os.system(f'savify "{mensagem}" -q best -f mp3 -o "./{config.pasta_downloads}"')
            upload.down(self.ids)
            #upload.sms2(self.ids, 'Quer receber as musica agora?')
            return f'Sua musica foi enviada 😊\n Muito obrigado por usar meu bot \natt\n@Dryrtan'
        
        elif 'album' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musicas, agorinha enviamos.')
            os.system(f'savify "{mensagem}"  -q best -f mp3 -o "./{config.pasta_downloads}"')
            upload.down(self.ids)
            #upload.sms2(self.ids, 'Quer receber as musicas agora?')
            return f'Todas as sua musicas foram enviadas 😊\n Muito obrigado por usar meu bot @Dryrtan'
        
        elif 'playlist' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musicas, agorinha enviamos.')
            os.system(f'savify "{mensagem}" -q best -f mp3 -o "./{config.pasta_downloads}"')
            upload.down(self.ids)
            #upload.sms2(self.ids, 'Quer receber as musicas agora?')
            return f'Todas as sua musicas foram enviadas 😊\n Muito obrigado por usar meu bot @Dryrtan'

        elif 'artist' in mensagem:
            upload.sms(self.ids, 'Estamos baixando sua musicas, agorinha enviamos.')
            os.system(f'savify "{mensagem}"  -q best -f mp3 -o "./{config.pasta_downloads}"')
            upload.down(self.ids)
            #upload.sms2(self.ids, 'Quer receber as musicas agora?')
            return f'Todas as sua musicas foram enviadas 😊\n Muito obrigado por usar meu bot @Dryrtan'

        elif 'episode' in mensagem:
            return f'''Eita, infelismente não posso fazer download de podcasts, desculpe, que tal uma música em?! '''

        elif mensagem.lower() in ('s', 'sim', '/sim'):
            upload.down(self.ids)
            return f'''Todas as sua musicas foram enviadas 😊\n Muito obrigado por usar meu bot @Dryrtan'''
        
        #elif mensagem.lower() in ('n', 'nao', '/nao'):
            #return f'''😬 Ok, apagando musicas do servidor...'''
        
        else:
            print(mensagem)
            return f'''Humm... acho melhor você da uma olhadinha nesse link, não consegui entender. 🤔 🤷🏻♂'''


    # Responde em texto
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}' 
        requests.get(link_requisicao)

Bot = TelegramBot()
Bot.Iniciar()
