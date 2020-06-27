###########################################################
# Vinicius Miranda de Pinho
# Junho de 2020
# POM para teste case da AME
# Cada elemento do app pode ser mudado nesta pagina.
#
###########################################################


class UserPage:
    # locator do app cadastro de cliente
    txt_banner_allow_id = "com.lbe.security.miui:id/permission_allow_button_1"
    txt_botao_mais_xpath = "//*[@class='android.widget.ImageButton']"
    txt_cadastrar_novo_xpath = "//*[@text='Cadastrar Novo']"
    txt_inserir_campo_nome_id = "br.com.dudstecnologia.cadastrodeclientes:id/editNome"
    txt_botao_salvar_xpath = "//*[@text='SALVAR']"
    txt_botao_ok_sucesso_xpath = "//*[@text='OK']"
    txt_clica_sobre_user_cadas_xpath = "//*[@text='Sem telefone']"
    txt_clica_excluir_xpath = "//*[@text='EXCLUIR']"
    txt_clica_sim_excluir_xpath = "//*[@text='SIM']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    def click_banner_allow(self):
        self.driver.find_element_by_id(self.txt_banner_allow_id).click()

    def click_button_mais(self):
        self.driver.find_element_by_xpath(self.txt_botao_mais_xpath).click()

    def click_novo_cadastro(self):
        self.driver.find_element_by_xpath(self.txt_cadastrar_novo_xpath).click()

    def inserir_campo_nome(self, user_name):
        self.driver.find_element_by_id(self.txt_inserir_campo_nome_id).send_keys(user_name)

    def click_salvar_cadastro(self):
        self.driver.find_element_by_xpath(self.txt_botao_salvar_xpath).click()

    def click_OK_salvar(self):
        self.driver.find_element_by_xpath(self.txt_botao_ok_sucesso_xpath).click()

    def back_button(self):
        self.driver.back()

# self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_button_1").click()
# self.driver.find_element_by_xpath("//*[@class='android.widget.ImageButton']").click()
# self.driver.find_element_by_xpath("//*[@text='Cadastrar Novo']").click()
# self.driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editNome").send_keys(name_user1)
# self.driver.find_element_by_xpath("//*[@text='SALVAR']").click()
# self.driver.find_element_by_xpath("//*[@text='OK']").click()
# self.driver.find_element_by_xpath("xpath=//*[@text='Sem telefone']").click()
# self.driver.find_element_by_xpath("xpath=//*[@text='EXCLUIR']").click()
# self.driver.find_element_by_xpath("xpath=//*[@text='SIM']").click()
# self.driver.back()
