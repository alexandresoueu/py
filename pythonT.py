from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'/Users/alexandreoliveira/Downloads/geckodriver')
driver.implicitly_wait(10)
driver.get('http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/')

def consultar():
    class_data = 'body > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > form:nth-child(7) > div:nth-child(2) > fieldset:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(3)'
    class_consulta = '/html/body/div[1]/div[1]/div/form/div/div[2]'

    data_today = '15012020'

    input_data = driver.find_element_by_css_selector(class_data)
    btn_search = driver.find_element_by_xpath(class_consulta)

    input_data.send_keys(data_today)
    btn_search.click()

consultar()