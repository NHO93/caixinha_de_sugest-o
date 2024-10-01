# Sistema de Caixinha de Sugestão Anônima

Este projeto é uma aplicação web simples onde os usuários podem enviar sugestões de forma anônima. As sugestões são enviadas diretamente para um e-mail configurado, sem o uso de um banco de dados. A aplicação é desenvolvida com **Python (Flask)** e estilizada com **CSS responsivo**.

## Funcionalidades

- Envio anônimo de sugestões.
- As sugestões são enviadas diretamente por e-mail.
- Mensagem de sucesso exibida após o envio.
- Design responsivo para garantir compatibilidade com dispositivos móveis.

## Requisitos

- **Python 3.x**
- **Pip** (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/NHO93/caixinha_de_sugestao.git
   cd caixinha_de_sugestao
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais de e-mail (e-mail e senha):
     ```bash
     EMAIL_USER=seuemail@gmail.com
     EMAIL_PASS=suasenha
     ```

5. **Inicie o servidor Flask:**
   ```bash
   python app.py
   ```

6. **Acesse a aplicação no navegador:**
   Abra o navegador e vá para: `http://127.0.0.1:5000/`

## Como Usar

- Acesse a página inicial da aplicação.
- Digite sua sugestão no campo de texto e clique no botão "Enviar Sugestão".
- Uma mensagem de sucesso será exibida na mesma página, confirmando que sua sugestão foi enviada com sucesso.

## Segurança

Certifique-se de que o arquivo `.env`, contendo suas credenciais de e-mail, **não seja adicionado ao Git**. O projeto já inclui um arquivo `.gitignore` que impede que esse arquivo seja enviado para o repositório.

---

### Deploy no Vercel

Para realizar o deploy da sua aplicação no Vercel, siga os passos abaixo:

1. **Instalar a CLI do Vercel:**
   ```bash
   npm install -g vercel
   ```

2. **Criar o arquivo `vercel.json`:**
   Na raiz do projeto, crie um arquivo chamado `vercel.json` com o seguinte conteúdo:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Configurar as variáveis de ambiente no Vercel:**
   - Acesse o painel de controle do Vercel.
   - Vá até sua aplicação e clique em "Settings" > "Environment Variables".
   - Adicione suas variáveis de ambiente `EMAIL_USER` e `EMAIL_PASS` com os valores apropriados.

4. **Fazer o Deploy:**
   No terminal, execute:
   ```bash
   vercel
   ```

5. **Verificar o Deploy:**
   Após o processo de deploy, um link será gerado. Acesse esse link no navegador para verificar se sua aplicação Flask está funcionando corretamente.

---

### Dependências

- **Flask**: Framework web utilizado para criar a aplicação.
- **python-dotenv**: Utilizado para carregar as variáveis de ambiente de forma segura.

---

Agora o sistema está pronto para ser utilizado e também pode ser facilmente hospedado no Vercel!