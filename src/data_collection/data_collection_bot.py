from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting a bigger timeout for communication between Selenium and ChromeDriver
CHROMEDRIVE_PATH = r"C:\Users\rafae\chromedriver-win64\chromedriver.exe"
chrome_service = Service(CHROMEDRIVE_PATH)  
driver = webdriver.Chrome(service=chrome_service)
driver.set_page_load_timeout(3000)  

BASE_URL = "https://reate.cprm.gov.br/arquivos/index.php/s/87Ny6plVJXljL0C"  

def navigate_and_download(path):
    # Remove "../" from the path
    parts = path.split("/")[2:]  

    # Accessing the page through the base url
    driver.get(BASE_URL)
    time.sleep(2)
    body = driver.find_element(By.TAG_NAME, "body")

    # Walking through the subdirectories
    for part in parts[:-1]:
        # Clicking on the header so the page gets focus
        header = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "headerName-container"))
        )
        header.click()

        nav_attempts = 50  
        while nav_attempts > 0:
            try:
                WebDriverWait(driver, 30).until(EC.any_of(EC.presence_of_element_located((By.CLASS_NAME, "innernametext"))))
                link = driver.find_element(By.LINK_TEXT, part)     
                link.click()
                time.sleep(2)
                break  
            except NoSuchElementException:
                print(f"Element {part} not found. Scrolling down...")
                body.send_keys(Keys.PAGE_DOWN) # Pressing the PAGE DOWN key
                time.sleep(1)
                nav_attempts -= 1
            except Exception as e:
                print(f"Exception: {e}")
                print(f"Exception when accessing {part}")
    
    # Downloading the file
    download_attempts = 50
    while download_attempts > 0:
        try:
            link = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f"//span[@class='innernametext' and text()='{parts[-1][:-6]}']"))
            )
            link.click()
            time.sleep(2)
            print(f"Download iniciado para: {parts[-1]}")
            break
        except NoSuchElementException:
            print(f"File {parts[-1]} not found. Scrolling down...")
            body.send_keys(Keys.PAGE_DOWN) # Pressing the PAGE DOWN key
            time.sleep(1)
            download_attempts -= 1
        except Exception as e:
            print(f"Exception: {e}")
            print(f"Excpetion when downloading {parts[-1]}")

with open("../data_selection/selected_wells_images.txt", "r", encoding="utf-8", errors="ignore") as file:
    for path in file:
        navigate_and_download(path)

input("Press Enter to close browser...")
driver.quit()
