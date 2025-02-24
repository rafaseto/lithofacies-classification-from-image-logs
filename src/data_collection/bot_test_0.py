from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do driver (mude para o caminho do seu WebDriver)
driver = webdriver.Chrome()

# URL base da página onde os arquivos estão listados
BASE_URL = "https://reate.cprm.gov.br/arquivos/index.php/s/87Ny6plVJXljL0C"  

def navegar_e_baixar(caminho):
    # Remove os "../" do caminho
    partes = caminho.split("/")[2:]  

    # Vai para a página inicial
    driver.get(BASE_URL)
    time.sleep(2)

    # Percorre as subpastas
    for parte in partes[:-1]:
        try:
            link = driver.find_element(By.PARTIAL_LINK_TEXT, parte)
            link.click()
            time.sleep(2)
        except Exception as e:
            print(f"Exception: {e}")
            print(f"Erro ao acessar: {parte}")
            return
    print(partes[-1][:-6])
    # Clica no arquivo para baixar
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, partes[-1][:-6]).click()
        print(f"Download iniciado para: {partes[-1]}")
    except Exception as e:
        print(f"Exception: {e}")
        print(f"Erro ao tentar baixar {partes[-1]}")

with open("../data_selection/selected_wells_images.txt", "r", encoding="utf-8", errors="ignore") as file:
    for path in file:
        navegar_e_baixar(path)

# Fecha o navegador
driver.quit()
