from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/')

time.sleep(5)

def consultar():
   # class_consulta = '/html/body/div[1]/div[1]/div/form/div/div[2]'
    driver.switch_to.frame("bvmf_iframe")
    data_today = '14/02/2020'
    time.sleep(4)
    element = driver.find_element_by_name('dData1')
    element.clear()
    element.send_keys(data_today)
    driver.find_element_by_xpath('//*[@id="divContainerIframeBmf"]/div[1]/div/form/div/div[2]/button').click()

    # element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'btnK')))
    # driver.execute_script("arguments[0].click();", element)
    #btn_search = driver.find_element_by_xpath(class_consulta)

#    input_data.send_keys(data_today)
 #   btn_search.click()

consultar()