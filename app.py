from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

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
        suggestion = request.form.get('suggestion', '').strip()

        # Verifica se a sugestão não está vazia
        if suggestion:
            try:
                # Envia a sugestão via e-mail
                send_email(suggestion)

                # Exibe a mensagem de sucesso
                flash('Sua sugestão foi enviada com sucesso!', 'success')
            except Exception as e:
                # Exibe a mensagem de erro
                flash('Houve um erro ao enviar sua sugestão. Por favor, tente novamente mais tarde.', 'danger')
                # Opcional: Log o erro para depuração
                app.logger.error(f'Erro ao enviar e-mail: {e}')
            return redirect(url_for('index'))
        else:
            flash('Por favor, insira uma sugestão.', 'danger')

    return render_template('index.html')

def send_email(suggestion):
    msg = EmailMessage()
    msg['Subject'] = 'Nova Sugestão Anônima'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f'Sugestão recebida: {suggestion}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)
