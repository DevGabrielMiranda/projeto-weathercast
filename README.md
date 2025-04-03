
# Previsão do tempo automatizada via Email / Automated Weather Forecast via Email
- Uma aplicação automatizada em Python que utiliza Selenium para buscar a previsão do tempo no site escolhido e envia as informações diretamente para o seu e-mail. Ideal para quem deseja receber atualizações diárias sobre as condições meteorológicas de uma cidade específica, sem esforço manual.
- An automated Python application that uses Selenium to fetch the weather forecast from a chosen website and send the information directly to your email. Ideal for those who want to receive daily updates on the weather conditions of a specific city, without manual effort.

# 🚀 Funcionalidades / Features:
- 📊 Coleta de Dados: Acessa o site tempo.com e extrai a temperatura atual, a condição climática e a previsão para os próximos 3 dias.
- 📧 Envio por E-mail: Formata os dados em um e-mail HTML e envia automaticamente para o destinatário configurado.
- ⏰ Agendamento Automático: Utiliza a biblioteca schedule para executar o script diariamente em um horário programado.

- 📊 Data Collection: Access the website tempo.com and extract the current temperature, weather conditions and the forecast for the next 3 days.
- 📧 Send by Email: Formats the data into an HTML email and automatically sends it to the configured recipient.
- ⏰ Automatic Scheduling: Uses the schedule library to run the script daily at a scheduled time.
# 🛠 Requisitos / Requirements:
Python 3.x instalado no sistema.
Google Chrome e Chrome WebDriver configurados corretamente.
# ⚙️ Configuração / Configuration:
Instale as dependências no terminal / Install all dependencials on CMD of your machine:

pip install schedule selenium webdriver-manager python-dotenv

Configure as credenciais de e-mail em um arquivo .env no mesmo diretório do script / Configure email credentials in a .env file in the same directory as the script
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=suasenha

Execute o script para testar o envio de e-mails / Execute the script for test the send to e-mails
python weather_email_scraper.py

# 🔍 Notas / Observations
- Certifique-se de que o Chrome WebDriver está instalado e atualizado (o webdriver-manager já facilita esse processo automaticamente).
Caso encontre problemas com a automação do navegador, tente atualizar o Google Chrome e o WebDriver.
- Have sure of the Chrome WebDriver are instaled and updated (the webdriver-manager alredy acess these process automaticad).
If you find some trouble with automation of browser, try update the Google Chrome and the WebDriver.
