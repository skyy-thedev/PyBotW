import json
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui 
import os 

# Ler dados do arquivo JSON
with open('clientes.json', 'r', encoding='utf-8') as arquivo_json:
    dados_clientes = json.load(arquivo_json)

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

for cliente in dados_clientes:
    # Extrair informações sobre nome, telefone e data de vencimento
    nome = cliente['Nome']
    telefone = cliente['Telefone']
    valor = cliente['Valor']
    vencimento = cliente['DataVencimento']
    
    mensagem = f'Olá {nome}, seu boleto de valor {valor} vence no dia {vencimento}. Favor pagar no link https://www.link_do_pagamento.com'

    # Criar links personalizados do WhatsApp e enviar mensagens para cada cliente
    # com base nos dados do arquivo JSON
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(12)
        seta = pyautogui.locateCenterOnScreen('seta.bmp')
        sleep(7)
        pyautogui.click(seta[0], seta[1])
        sleep(10)
        pyautogui.hotkey('ctrl', 'w')
        sleep(10)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone},{valor}{os.linesep}')
print('Todos os contatos foram cobrados com sucesso.')