from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash'  # Necessário para o uso do flash messages

# Carrega as variáveis de e-mail e senha do arquivo .env
EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        suggestion = request.form['suggestion']

        # Verifica se a sugestão não está vazia
        if suggestion:
            # Envia a sugestão via e-mail
            send_email(suggestion)

            # Exibe a mensagem de sucesso
            flash('Sua sugestão foi enviada com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Por favor, insira uma sugestão.', 'danger')

    return render_template('index.html')

def send_email(suggestion):
    # Garantindo que a sugestão seja tratada como string UTF-8
    suggestion_utf8 = suggestion.encode('utf-8', errors='ignore').decode('utf-8')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Nova Sugestão Anônima'
        body = f'Sugestão recebida: {suggestion_utf8}'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

if __name__ == "__main__":
    app.run(debug=True)
