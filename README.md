
# Weather Email Scraper
Uma aplicação automatizada em Python que utiliza Selenium para buscar a previsão do tempo no tempo.com e envia as informações diretamente para o seu e-mail. Ideal para quem deseja receber atualizações diárias sobre as condições meteorológicas de uma cidade específica, sem esforço manual.

# 🚀 Funcionalidades:
📊 Coleta de Dados: Acessa o site tempo.com e extrai a temperatura atual, a condição climática e a previsão para os próximos 3 dias.
📧 Envio por E-mail: Formata os dados em um e-mail HTML e envia automaticamente para o destinatário configurado.
⏰ Agendamento Automático: Utiliza a biblioteca schedule para executar o script diariamente em um horário programado.
# 🛠 Requisitos:
Python 3.x instalado no sistema.
Google Chrome e Chrome WebDriver configurados corretamente.
# ⚙️ Configuração:
Instale as dependências no terminal:

pip install schedule selenium webdriver-manager python-dotenv

Configure as credenciais de e-mail em um arquivo .env no mesmo diretório do script:
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=suasenha

Execute o script para testar o envio de e-mails:
python weather_email_scraper.py

# 🔍 Notas
Certifique-se de que o Chrome WebDriver está instalado e atualizado (o webdriver-manager já facilita esse processo automaticamente).
Caso encontre problemas com a automação do navegador, tente atualizar o Google Chrome e o WebDriver.
