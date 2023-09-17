#importando selenium e webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#Abrindo Chrome
options = Options()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

(navegador) = webdriver.Chrome(options=options)

#Abrindo Rewards --> PERSONALIZE! o email e senha

navegador.get("https://rewards.bing.com")
navegador.find_element('xpath','//*[@id="i0116"]').send_keys('fabriziommoura@gmail.com')
navegador.find_element('xpath','//*[@id="idSIButton9"]').click()
navegador.find_element('xpath','//*[@id="i0118"]').send_keys('8002fabrizio')
time.sleep(2)
navegador.find_element('xpath','//*[@id="idSIButton9"]').click()
navegador.find_element('xpath','//*[@id="idBtn_Back"]').click()
time.sleep(3)
navegador.find_element('xpath','//*[@id="ma-card-link"]/span').click()
time.sleep(3)
navegador.get("https://www.bing.com/search?q=gg&FORM=HDRSC1")

#Ciclo para digitar no bing 

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()
time.sleep(1)
navegador.find_element('xpath','//*[@id="bnp_btn_accept"]').click()
time.sleep(1)
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()
time.sleep(1)
navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

navegador.find_element('xpath','//*[@id="sb_form_q"]').send_keys('i')
navegador.find_element('xpath','//*[@id="sb_form_go"]').click()

#Developed by @fabriziommoura