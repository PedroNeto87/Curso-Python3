import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except (urllib.erro.URLError):
    print(f'O site PUDIM não está disponível no momento.')
else:
    print(f'Consegui acessar o site PUDIM com sucesso!')
