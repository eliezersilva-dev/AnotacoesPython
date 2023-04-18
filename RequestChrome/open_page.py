from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


def chamar_pagina():
    options = Options()
    options.add_argument('--headless')
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)
    navegador.get('https://github.com/eliezersilva-dev')

    sleep(10)


chamar_pagina()
