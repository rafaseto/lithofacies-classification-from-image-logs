import os
import time
from tkinter import Tk, filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# URL base para acesso aos arquivos
BASE_URL = "https://reate.cprm.gov.br/arquivos/index.php/s/UIgVZobfQwyLeA1"

# Configurações do ChromeDriver
CHROMEDRIVER_PATH = r"C:\Users\rafae\chromedriver-win64\chromedriver.exe"
chrome_service = Service(CHROMEDRIVER_PATH)
options = Options()
# Define diretório padrão de download e desativa prompt
download_dir = os.path.join(os.getcwd(), 'downloads')
os.makedirs(download_dir, exist_ok=True)
options.add_experimental_option('prefs', {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'profile.default_content_settings.popups': 0
})
options.page_load_strategy = "none"


def select_input_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo .txt de caminhos",
        filetypes=[("Arquivos de Texto", "*.txt")]  
    )
    root.destroy()
    return file_path


def navigate_and_download(path, driver):
    # Remove prefix de diretórios indesejados
    parts = path.strip().split("/")[2:]

    # Acessa a URL base
    driver.get(BASE_URL)
    time.sleep(2)
    driver.execute_script("window.stop();")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")

    # Navega pelas pastas
    for part in parts[:-1]:
        header = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "headerName-container"))
        )
        header.click()
        attempts = 50
        while attempts > 0:
            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "innernametext"))
                )
                link = driver.find_element(By.LINK_TEXT, part)
                link.click()
                time.sleep(2)
                break
            except NoSuchElementException:
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
                attempts -= 1
            except Exception:
                time.sleep(1)
                attempts -= 1

    # Clica para download do arquivo
    filename = parts[-1]
    name_without_ext = os.path.splitext(filename)[0]
    attempts = 50
    while attempts > 0:
        try:
            # Encontra o elemento <a> que contenha o nome do arquivo
            span = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH,
                    f"//span[@class='innernametext' and text()='{name_without_ext}']"))
            )
            link = span.find_element(By.XPATH, './ancestor::a')
            link.click()
            WebDriverWait(driver, 10).until(lambda d: os.path.exists(os.path.join(download_dir, filename)))
            print(f"Download concluído: {filename}")
            break
        except NoSuchElementException:
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            attempts -= 1
        except Exception:
            time.sleep(1)
            attempts -= 1


def main():
    # Seleciona arquivo de caminhos via explorador
    input_file = select_input_file()
    if not input_file:
        print("Nenhum arquivo selecionado. Encerrando.")
        return

    # Inicializa o driver
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.set_page_load_timeout(300)

    # Lê cada caminho e faz download
    with open(input_file, "r", encoding="utf-8", errors="ignore") as file:
        for path in file:
            attempts = 100
            while attempts > 0:
                try:
                    navigate_and_download(path, driver)
                    break
                except (TimeoutException, TimeoutError):
                    print("Timeout ao carregar página. Tentando novamente...")
                    attempts -= 1
                    time.sleep(5)

    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    main()
