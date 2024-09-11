"""
Bot para whatsapp onde le arquivo xlsm com dados dos nomes e numeros que tenho interesse em mandar mensagem pelo bot

"""
#bibliotecas usadas no script

import openpyxl 
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os

#estabelecer comunicação com site da whatsapp
webbrowser.open('https://web.whatsapp.com/')
sleep(10)

#Ler documento salvo com os nomes e numeros dos contatos
workbook = openpyxl.load_workbook('number_cel.xlsx')
pagina_clientes = workbook['Planilha1']

#informando para a condição comecar na segunda linha do arquivo (exemplo foi um xlsm)
for linha in pagina_clientes.iter_rows(min_row= 2):

    nome = linha[0].value
    telefone = linha[1].value
    mensagem = f'Ola {nome} meu pix parceiro {telefone} ta maluco'
   
    #Criar link customizado pelo proprio python e enviar a mensagem de acordo com o documento 
    #criando uma estrutura de ero onde foi usado um documento csv(com vigula) para salvamento de erros durante o envio das mensagens 
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        seta = pyautogui.locateCenterOnScreen('envio_whatsapp.png')
        sleep(5)
        pyautogui.click(seta[0],seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'não foi possivel enviar mensagem para {nome}')
        with open('erros.csv','a',newline='',encoding='utf8') as arquivo: arquivo.write(f'{telefone},{nome}{os.linesep}')


 