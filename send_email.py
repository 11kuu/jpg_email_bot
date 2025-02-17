import pandas as pd
import os 
import smtplib
from email.message import EmailMessage
import yfinance as yf
import matplotlib.pyplot as plt
import mplcyberpunk

diretorio = os.getcwd()
os.chdir(diretorio)
download = yf.download("BBAS3.SA")
download = download['Close']
download.dropna()
download.plot()

plt.style.use('cyberpunk')
plt.plot(download)
plt.savefig('BRAZIL_BANK.png')


# Email
send = str(input('enter the email you will send [ to_send_domain@domain.com ] :')).lower()
receive = str(input('enter the email you will receive [ your_domain@domain.com ] :')).lower()

email = 'your_email@domain.com'

with open('C:/Users/linco/Documents/Visual Studio Projects/csv_email/password.txt') as f:
    senha = f.readlines()
    
    f.close()

senha_do_email = senha[0]


msg = EmailMessage()
msg['Subject'] = 'Enviando e-mail'
msg['From'] = send
msg['To'] = receive
msg.set_content(f'Here is the graph plotted from Banco do Brasil :')

with open('BRAZIL_BANK.png', 'rb') as content_file :
    content = content_file.read()
    msg.add_attachment(content, maintype = 'application', subtype = 'png', filename = 'BRAZIL_BANK.png')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email, senha_do_email)
        smtp.send_message(msg)

