import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import os 
import smtplib
from email.message import EmailMessage

diretorio = os.getcwd()
os.chdir(diretorio)

dados = pd.read_csv('Mundo9dfp_cia_aberta_DRE_con_2021.csv', sep = ';',
                        encoding= "ISO-8859-1",
                        decimal= ',',
                        index_col= 'DT_REFER',
                        usecols= ['DT_REFER', 'DENOM_CIA', 'ESCALA_MOEDA', 'ORDEM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA'])


save = dados.to_csv('data.csv')

email = 'your_email@example.com'


with open('password_api.txt') as f:
    senha = f.readlines()
    
    f.close()

senha_do_email = senha[0]

msg = EmailMessage()
msg['Subject'] = 'Enviando e-mail'
msg['From'] = 'your_email@your_domain.com'
msg['To'] = 'to_send_email_address'
msg.set_content(f'the index.csv:')

with open('data.csv', 'rb') as content_file :
    content = content_file.read()
    msg.add_attachment(content, maintype = 'application', subtype = 'csv', filename = 'data.csv')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email, senha_do_email)
        smtp.send_message(msg)

