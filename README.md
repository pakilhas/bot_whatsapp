# WhatsApp Bot para Envio de Mensagens

Este projeto é um bot para WhatsApp que lê um arquivo XLSM contendo nomes e números de telefone e envia mensagens personalizadas para cada contato. A automação é feita utilizando Python e várias bibliotecas para interação com o WhatsApp Web.

## Bibliotecas Usadas

- `openpyxl`: Para ler o arquivo XLSM contendo os dados dos contatos.
- `urllib.parse`: Para criar links customizados para o WhatsApp.
- `webbrowser`: Para abrir o link do WhatsApp Web no navegador.
- `pyautogui`: Para interagir com a interface do WhatsApp Web e enviar mensagens.
- `time`: Para adicionar delays e garantir que as ações sejam realizadas corretamente.
- `os`: Para manipulação de arquivos e diretórios.

## Funcionalidades

1. **Abrir WhatsApp Web**: O bot abre o WhatsApp Web no navegador.
2. **Ler Dados de Contatos**: Lê um arquivo XLSM contendo os nomes e números dos contatos.
3. **Enviar Mensagens**: Para cada contato, cria um link de mensagem personalizado e o envia via WhatsApp Web.
4. **Tratamento de Erros**: Caso ocorra algum erro durante o envio da mensagem, o número e nome do contato são registrados em um arquivo CSV.

## Requisitos

Certifique-se de que você tem as seguintes bibliotecas instaladas:

```bash
pip install openpyxl pyautogui
```
Além disso, você precisará:

    Um arquivo XLSM chamado number_cel.xlsx contendo os nomes e números dos contatos.
    Uma imagem envio_whatsapp.png que representa o botão de envio no WhatsApp Web (para usar com pyautogui).

Como Usar

    Preparar o Arquivo:
        Crie um arquivo XLSM chamado number_cel.xlsx com duas colunas: uma para o nome e outra para o número de telefone.
        Coloque a imagem envio_whatsapp.png no mesmo diretório do script. Esta imagem deve ser uma captura de tela do botão de envio do WhatsApp Web.

    Executar o Script:
        Certifique-se de que o WhatsApp Web está configurado e que você está logado na sua conta.
        Execute o script Python.
    Verificar Resultados:

        O bot abrirá o WhatsApp Web e começará a enviar mensagens.
        Caso ocorra algum erro, os detalhes dos contatos não processados serão registrados no arquivo erros.csv.

## Notas
O script pode exigir ajustes no tempo de espera (sleep) dependendo da velocidade da sua conexão e do desempenho do seu computador.
Certifique-se de que a imagem envio_whatsapp.png está atualizada e corresponde ao botão de envio do WhatsApp Web.

# Opa, 
| Rede Social |                                            |
|-------------|-----------------------------|

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pablo-carvalho-93927a220/)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=fff)](https://www.instagram.com/pablo_ddh/) [![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=fff)](https://discord.com/channels/1235957312477466717/1235957313076985858)
[![GitHub](https://img.shields.io/badge/GitHub-%23181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pakilhas)

[![DIO](https://img.shields.io/badge/D%20I%20O-%23FFF100?style=for-the-badge&logo=digitalocean&logoColor=black)](https://web.dio.me/users/pakilhas?tab=achievements)