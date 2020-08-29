from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random

class InstagramBot:
    def __init__(self, username, password): #consultor
        self.username = username    #}atribui valores para login
        self.password = passsword    #}
        self.driver = webdriver.Firefox(executable_path="C:\webdrivers\geckodriver.exe") # caminhogeckodriver aqui

    def login(self):    #validacao de login
        driver = self.driver    #passando informacoes do firefox para o selenium
        driver.get('https://www.instagram.com') #passando sitio
        time.sleep(4) 
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")#pesquisa no html a seguinte tag do bt
        login_button.click()    #efetua o click sobre a tag encontrada
        
        #após essas acoes o sistema carrega a tela de login
        
        user_element = driver.find_element_by_xpath("//input[@name='username']")#pesquisa a tag username no html
        user_element.clear()#limpa toda a tag encontrada afim de nao deixar rastros
        user_element.send_keys(self.username)#envia de forma instantanea a username(nome do usuario) 
        password_element = driver.find_element_by_xpath("//input[@name='password']")#pesquisa a tag password(senha)
        password_element.clear()#limpa toda a tag encontrada afim de nao deixar rastros
        password_element.send_keys(self.password)#envia de forma instantanea a password(senha do usuario)
        password_element.send_keys(Keys.RETURN)#a funcao return simula o botao enter no teclado
        time.sleep(8)
        
        hashtags=["computacao", "tecnologia"]
        self.comentar_nas_fotos(random.choice(hashtags)) #Altere aqui para a hashtag que você deseja usar.
  
    @staticmethod
    def humano(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)#simula digitacao humana
    
    def comentar_nas_fotos(self,hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')#joga a pesquisa desejada no navegador
        time.sleep(3)
        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')    
            time.sleep(6)
        hrefs = driver.find_elements_by_tag_name('a')#procura elementos com a tag a(fotos)
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]#captura o link das fotos
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))#testa a quantidae de fotos retornada por rolagem do scroll

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                driver.find_element_by_xpath("//button[@class='dCJp8 afkep']").click()
                time.sleep(2)
                comentarios = ["que legal", "muito bom"] 
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2, 5))
                self.humano(random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(30, 40))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(3)
            except Exception as e:
                print(e)
                time.sleep(3)
instabot = InstagramBot('user','pass') # entrar com o usuário e senha aqui
instabot.login()