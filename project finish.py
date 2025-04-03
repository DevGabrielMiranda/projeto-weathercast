import schedule
import time
import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv  # Importa a função para carregar variáveis do arquivo .env
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Função para iniciar o navegador
def iniciar_driver():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), 
        options=chrome_options
    )
    return driver

# Função principal que coleta o clima e envia o e-mail
def enviar_previsao():
    driver = iniciar_driver()
    driver.get('https://www.tempo.com/jacarei_sao-paulo-l115835.htm')

    try:
        temperatura = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.dato-temperatura.changeUnitT'))
        ).text
        condicao_weather = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.descripcion'))
        ).text

        data_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.subtitle-m')]
        previsao_condicao_climatica_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.descripcion')]
        previsao_max_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.max.changeUnitT')]
        previsao_min_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.min.changeUnitT')]

        # Criar a mensagem formatada em HTML
        mensagem = f"""
        <html>
            <body>
                <p>Hi there, here's your weather forecast:</p>
                <p><strong>Temperatura atual em Jacareí:</strong> {temperatura}°</p>
                <p><strong>Condição atual:</strong> {condicao_weather}</p>
                <h3>Previsão para os próximos 3 dias:</h3>
                <ul>
        """
        for i in range(1, 4):
            mensagem += f"""
                <li>
                    <strong>Day {data_text[i]}</strong><br>
                    Condição: {previsao_condicao_climatica_text[i]}<br>
                    Temp Max e Min: {previsao_max_text[i]} - {previsao_min_text[i]}
                </li>
                <br>
            """

        mensagem += """
                </ul>
                <p>Keep checking your email daily for updates. Bye!</p>
            </body>
        </html>
        """

        # Usando as variáveis de ambiente para pegar o e-mail e senha
        EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  # Pega o e-mail da variável de ambiente
        EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Pega a senha da variável de ambiente


        mail = EmailMessage()
        mail['Subject'] = 'Weather Forecast'
        mail['From'] = EMAIL_ADDRESS
        mail['To'] = 'soaresbiel2134@gmail.com'
        mail.add_header('Content-Type', 'text/html')
        mail.set_payload(mensagem.encode('utf-8'))

        # Enviar e-mail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
            email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            email.send_message(mail)

        print('E-mail enviado com sucesso!')

    except Exception as e:
        print(f'Erro ao buscar os dados: {e}')
    
    finally:
        driver.quit()

# Agendar para rodar todo dia às 07:00 da manhã
schedule.every().day.at("20:45").do(enviar_previsao)

print("Agendador iniciado. O e-mail será enviado diariamente às 20:45.")

# Loop para manter o agendamento rodando
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica o agendamento a cada minuto
