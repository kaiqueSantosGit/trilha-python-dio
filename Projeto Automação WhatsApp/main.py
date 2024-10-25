from selenium import webdriver
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Especificando o caminho para o ChromeDriver
service = Service(r'C:\Users\kaiqu\Documents\.vscode\Projeto Automação WhatsApp\chromedriver-win64')

# Inicializando o WebDriver com o Service
driver = webdriver.Chrome(service=service)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Espera o usuário escanear o código QR
input("Pressione Enter após escanear o código QR")

# Localiza a conversa desejada
contato = "Rudney Gostoso Jr"
search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.click()
search_box.send_keys(contato)
search_box.send_keys(Keys.RETURN)

# Roteiro de mensagens
mensagens = [
    "Oi, tudo bem?",
    "Gostaria de compartilhar algumas informações importantes...",
    "Aqui está o primeiro ponto: ...",
    "Se precisar de mais detalhes, estou à disposição!"
]

# Envia as mensagens do roteiro
for mensagem in mensagens:
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(mensagem)
    message_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Intervalo entre mensagens

# Fecha o navegador
driver.quit()
