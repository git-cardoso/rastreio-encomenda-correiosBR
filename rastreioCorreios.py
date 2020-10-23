from selenium import webdriver
from time import  sleep

navegador="/chromedriver"
titiogoogle = webdriver.Chrome(executable_path=navegador)
titiogoogle.get('https://www2.correios.com.br/sistemas/rastreamento/default.cfm')

titiogoogle.find_element_by_id('objetos').send_keys('codigo')



titiogoogle.find_element_by_id('btnPesq').click()



caminho  = titiogoogle.find_element_by_class_name('sroLbEvent').get_attribute("outerHTML")
status  = titiogoogle.find_element_by_class_name('ctrlcontent').get_attribute("outerHTML")
sleep(2)
print(caminho)
sleep(4)
print(status)
sleep(4)
titiogoogle.close()
