import time
import playsound as playsound
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager

# ENG
# log in to the discord via QR-code

# RU
# Заходим в дисик с телефона и входим в него через qr-код
# Мне лень вот эти все вводы и капчу прописывать

# DATA
# данные древних
name = "Eerikkie" # <- Ник чела (на конце "#" писать)
start = 1 # <- С какого тега начинать (1 = 0001)
end = 10000 # <- На каком теге закончить (10000 = 9999)

name = str(name + "#")

useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
options.add_argument("--window-size=1200,900")


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s, options=options)

try:
    driver.get(url="https://discord.com/channels/@me/")
    time.sleep(10)

    # клик по настройкам
    e = driver.find_element(By.XPATH, ("/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/section/div/div[3]/div[5]"))
    e.click()
    time.sleep(1)

    for i in range(start, end):

        if i < 10:
            i = str(i)
            i = '000' + i

        elif i < 100:
            i = str(i)
            i = '00' + i

        elif i < 1000:
            i = str(i)
            i = '0' + i

        i = str(i)
        res = str(name + i)

# FINDING
# находим чела

        q = driver.find_element(By.XPATH, ("/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/header/form/div[2]/input"))
        # не удалять таймслип
        time.sleep(1)
        q.send_keys(res)
        q.send_keys(u'\ue007')
        q.clear()
        time.sleep(1)

# CLOSING MODAL WINDOW
# закрывание модалки

        f = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div/form/div[2]/button")
        f.click()
        print(res + " - [X]")

# WHEN FOUND
# типа нашли чела

        try:
            x = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/header/form/div[3]")
            continue
        except NoSuchElementException:
            print(' - [FOUND]')
            playsound('sound.mp3') # Slax - Mimika Euphorica


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()