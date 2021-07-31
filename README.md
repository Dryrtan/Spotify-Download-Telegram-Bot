# Spotify-Download-Telegram-Bot
Bot criado no telegram para fazer downloads de musicas, playlists e discografia de artistas usando o Spotdl -> https://github.com/ritiek/spotify-downloader
##
O Funcionamento é muito simples, envie um link de música, playlist ou discografia do artista e o bot fará o resto, normalmente ele demora um pouco para fazer o download de listas de músicas, por se tratar de muitas músicas.
##
Você pode acessar ele atraves do link dele no Telegram -> http://t.me/Dryrtanbot
##

## O que é preciso para fazer funcionar na sua maquina??
- Primeiro vamos começar instalando as dependencias
```shell
sudo apt update && sudo apt install python3 -y
sudo apt install python3-pip -y
sudo pip3 install savify
sudo apt install ffmpeg
sudo pip install python-telegram-bot
```

- Mas se você preferir pode usar esse comando em conjunto
```shell
sudo apt update && sudo apt install python3 python3-pip ffmpeg -y && sudo pip3 install spotdl python-telegram-bot
```

- Após isso mudaremos o token do bot do Telegram
```python
def __init__(self):
        token = 'COLOQUE O TOKEN DO BOT AQUI'
        self.url_base = f'https://api.telegram.org/bot{token}/'
```
- Mudaremos o token no upload.py
```python
TOKEN = 'COLOQUE O TOKEN DO BOT AQUI'
bot = telegram.Bot(token=TOKEN)
```

##
![alt text](https://uploaddeimagens.com.br/images/003/285/772/original/Fluxograma.png?1623486888)
