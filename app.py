from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os
from dotenv import load_dotenv

# Carrega variaveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash'  # Necessário para o uso do flash messages

# Carrega as variaveis de e-mail e senha do arquivo .env
EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        suggestion = request.form['suggestion']
        
        # Envia a sugestao via e-mail
        send_email(suggestion)
        
        # Exibe a mensagem de sucesso
        flash('Sua sugestao foi enviada com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html')

def send_email(suggestion):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        subject = 'Nova Sugestao Anonima'
        body = f'Sugestao recebida: {suggestion}'
        
        msg = f'Subject: {subject}\n\n{body}'
        
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

if __name__ == "__main__":
    app.run(debug=True)