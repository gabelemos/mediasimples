import customtkinter as ctk
from tkinter import simpledialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Variáveis globais para armazenar username e password
username = ""
password = ""

# Configurações do customtkinter
ctk.set_appearance_mode("dark")  # Modo noturno
ctk.set_default_color_theme("blue")  # Tema azul

def inserir_login():
    global username, password
    # Criar pop-up de inserção de dados
    username = simpledialog.askstring("Login", "Insira seu nome de usuário: ")
    password = simpledialog.askstring("Login", "Insira sua senha: ", show='*')
    
    if username and password: 
        messagebox.showinfo("Sucesso", "Login salvo com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, insira seus dados novamente.")
        
def visualizar_notas():
    global username, password
    if not username or not password:
        messagebox.showwarning("Atenção", "Por favor, insira seus dados novamente.")
        return
    
    # Inicia o Selenium e abre o site 
    driver = webdriver.Chrome()
    driver.get("https://www.siepe.educacao.pe.gov.br/")

    # Aguardando carregar a página
    time.sleep(5)
    
    # Procurando o campo de login e senha e realizando o login
    try:
        campo_username = driver.find_element(By.NAME, "login")
        campo_senha = driver.find_element(By.NAME, "senha")
        btn_submit = driver.find_element(By.NAME, "btnOk")
        
        campo_username.send_keys(username)
        campo_senha.send_keys(password)
        
        btn_submit.click()
        
        # Aguarda o carregamento da próxima página
        time.sleep(1)  # Ajuste o tempo conforme necessário

        # Clica no botão com name "EWBaseForm32108013"
        btn_ew_base_form = driver.find_element(By.CLASS_NAME, "ac-icon-recepcao-alunos")
        btn_ew_base_form.click()

        # Aguarda 1 segundo
        time.sleep(1)

        # Clica no botão com class "ListaSelecaoDependentes"
        btn_lista_selecao = driver.find_element(By.CLASS_NAME, "ListaSelecaoDependentes")
        btn_lista_selecao.click()

        # Aguarda 1 segundo
        time.sleep(1)

        # Clica no primeiro <li> da <ul> com id "divBoletim_8051930"
        primeiro_li = driver.find_element(By.CSS_SELECTOR, "#divBoletim_8051930 li")
        primeiro_li.click()

        # Aguarda a nova janela abrir
        time.sleep(5)  # Ajuste o tempo conforme necessário

        # Alterna para a nova janela
        driver.switch_to.window(driver.window_handles[1])  # Muda para a nova janela

        # Aguarda a página carregar
        time.sleep(5)  # Ajuste o tempo conforme necessário

        # Captura os valores das <td> com as classes especificadas
        disciplinas = driver.find_elements(By.CLASS_NAME, "tdDisciplina")
        medias = {
            "Periodo1": driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo1") + driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo1 esconder"),
            "Periodo2": driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo2") + driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo2 esconder"),
            "Periodo3": driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo3") + driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo3 esconder"),
            "Periodo4": driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo4") + driver.find_elements(By.CLASS_NAME, "tdMediaPeriodo4 esconder"),
        }

        # Armazena os valores em um dicionário
        notas = {}
        disciplinas_desejadas = ["Biologia", "Física", "Geografia", "História", "Língua Inglesa", "Língua Portuguesa", "Matemática", "Química"]
        for i, disciplina in enumerate(disciplinas):
            disciplina_nome = disciplina.text
            if disciplina_nome in disciplinas_desejadas:
                notas[disciplina_nome] = {
                    "Periodo1": medias["Periodo1"][i].text if i < len(medias["Periodo1"]) else "0",
                    "Periodo2": medias["Periodo2"][i].text if i < len(medias["Periodo2"]) else "0",
                    "Periodo3": medias["Periodo3"][i].text if i < len(medias["Periodo3"]) else "0",
                    "Periodo4": medias["Periodo4"][i].text if i < len(medias["Periodo4"]) else "0",
                }

        # Exibe as notas formatadas
        for disciplina, valores in notas.items():
            media1 = float(valores["Periodo1"].replace(',', '.').strip())
            media2 = float(valores["Periodo2"].replace(',', '.').strip())
            media3 = float(valores["Periodo3"].replace(',', '.').strip())
            media4 = float(valores["Periodo4"].replace(',', '.').strip())
            total = media1 + media2 + media3 + media4
            mensagem = f"Suas notas em {disciplina} até o momento são: 1ª - {media1} | 2ª - {media2} | 3ª - {media3} | 4ª - {media4} | Soma total: {total}"
            messagebox.showinfo("Notas", mensagem)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro! {e}")
    finally:
        time.sleep(10)
        
# Criação da janela principal
root = ctk.CTk()  # Usando CTk em vez de Tk
root.title("Sistema de Notas")
root.geometry("640x300")

# Adicionando um rótulo (label) com texto
label_titulo = ctk.CTkLabel(root, text="Bem-vindo ao SIEPezinho!", font=("Arial", 16))
label_titulo.pack(pady=10)
label_titulo = ctk.CTkLabel(root, text="O seu poupa-tempo em calcular notas!", font=("Arial", 13))
label_titulo.pack(pady=10)

# Frame para organizar os rótulos de username e senha
frame_login = ctk.CTkFrame(root)
frame_login.pack(pady=10)
    
label_nome = ctk.CTkLabel(frame_login, text="username: ", font=("Arial", 12))
label_nome.pack(side="left", padx=(0, 10))  # Adiciona um espaço à direita

label_nome2 = ctk.CTkLabel(frame_login, text="---------", font=("Arial", 12))
label_nome2.pack(side="left")  # Adiciona o rótulo ao lado do username

label_senha = ctk.CTkLabel(frame_login, text="senha: ", font=("Arial", 12))
label_senha.pack(side="left", padx=(20, 10))  # Adiciona um espaço à direita

label_senha2 = ctk.CTkLabel(frame_login, text="---------", font=("Arial", 12))
label_senha2.pack(side="left")  # Adiciona o rótulo ao lado da senha
# Rótulos para username e senha

# Botão para inserir login
btn_inserir_login = ctk.CTkButton(root, text="Inserir Login", command=inserir_login, corner_radius=10)
btn_inserir_login.pack(pady=10)

# Botão para visualizar notas
btn_visualizar_notas = ctk.CTkButton(root, text="Visualizar Notas", command=visualizar_notas, corner_radius=10)
btn_visualizar_notas.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()