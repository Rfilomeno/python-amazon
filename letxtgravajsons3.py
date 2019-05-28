
import boto3
import json
dicionario = {}
linhas = []
lista=[]


def leitura_arquivo():
    arquivo = open('listagem.txt', 'r')
    return arquivo

def formata_dados(arquivo):
    arquivo = arquivo.read().splitlines()
    for item in arquivo:
        linhas.append(item.split(','))

    for i in range(0,len(linhas)):
        dicionario = dict(maquina=linhas[i][0],core=linhas[i][1],memoria=linhas[i][2],storage=linhas[i][3])
        lista.append(dicionario)
    return lista

def cria_arquivo(lista):
    with open('dados.json','w') as arquivo:
        arquivo.write(json.dumps(lista, indent=4))

def publica_arquivo():
    AWS_ACCESS_KEY_ID = 'chave amazon'
    AWS_SECRET_ACESS_KEY = 'chave amazon'

    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACESS_KEY,
    )
    s3 = session.resource('s3')
    s3.Object('infnetprojetopython', 'dados2.json').upload_file('dados.json')


arquivo = leitura_arquivo()
lista = formata_dados(arquivo)
cria_arquivo(lista)
publica_arquivo()







