from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
import time

# Define um timeout maior para a comunicação entre o Selenium e o ChromeDriver
CHROMEDRIVE_PATH = r"C:\Users\rafae\chromedriver-win64\chromedriver.exe"
chrome_service = Service(CHROMEDRIVE_PATH)  # Caminho para o chromedriver
driver = webdriver.Chrome(service=chrome_service)
driver.set_page_load_timeout(3000)  # Timeout maior (300 segundos)

BASE_URL = "https://reate.cprm.gov.br/arquivos/index.php/s/87Ny6plVJXljL0C"  

def navigate_and_download(caminho):
    # Remove "../" from the path
    partes = caminho.split("/")[2:]  

    # Accessing the page through the base url
    driver.get(BASE_URL)
    time.sleep(2)

    body = driver.find_element(By.TAG_NAME, "body")

    # Walking through the subdirectories
    for parte in partes[:-1]:
        header = driver.find_element(By.ID, "headerName-container")
        header.click()
        attempts = 50  
        while attempts > 0:
            try:
                link = driver.find_element(By.PARTIAL_LINK_TEXT, parte)       
                link.click()
                time.sleep(2)
                break  
            except NoSuchElementException:
                print(f"Element '{parte}' not found. Scrolling down...")
                body.send_keys(Keys.PAGE_DOWN) # Pressing the PAGE DOWN key
                time.sleep(1)
                attempts -= 1
            except Exception as e:
                print(f"Exception: {e}")
                break  
    print(partes[-1][:-6])
    
    # Downloading the file
    attempts = 50
    while attempts > 0:
        try:
            driver.find_element(By.PARTIAL_LINK_TEXT, partes[-1][:-6]).click()
            time.sleep(2)
            print(f"Download iniciado para: {partes[-1]}")
            break
        except NoSuchElementException:
            print(f"File {partes[-1]} not found. Scrolling down...")
            body.send_keys(Keys.PAGE_DOWN) # Pressing the PAGE DOWN key
            time.sleep(1)
            attempts -= 1
        except Exception as e:
            print(f"Exception: {e}")
            print(f"Excpetion when downloading {partes[-1]}")

with open("../data_selection/selected_wells_images.txt", "r", encoding="utf-8", errors="ignore") as file:
    for path in file:
        navigate_and_download(path)

input("Press Enter to close browser...")
driver.quit()
