#Imports
import pyautogui
import time
import pandas as pd

#Definir o tempo de espera
pyautogui.PAUSE = 0.5
#Variaveis
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

#Passo a passo
# Passo 1 Abrir o navegador e acessar o site
pyautogui.press("win")
time.sleep(1)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(1)
# Passo 2 Fazer o login no site de cadastro
pyautogui.press('tab')
pyautogui.write('yan@gmail.com')
pyautogui.press('tab')
pyautogui.write('pyton@123')
pyautogui.press('enter')

# Passo 3 importar a base de dados
base = pd.read_csv('produtos.csv')
print(base)

for linha in base.index:

  # Passo 3.1 Cadastrar primeiro produto
    #Código do produto
  pyautogui.click(x=852, y=257)
  pyautogui.write(str(base.loc[linha, 'codigo']))
    #Marca do produto
  pyautogui.press('tab')
  pyautogui.write(str(base.loc[linha, 'marca']))
    #Tipo do produto
  pyautogui.press('tab')
  pyautogui.write(str(base.loc[linha, 'tipo']))
    #Categoria do produto
  pyautogui.press('tab')
  pyautogui.write(str(base.loc[linha, 'categoria']))
    #Preço unitário do produto
  pyautogui.press('tab')
  pyautogui.write(str(base.loc[linha, 'preco_unitario']))
    #Custo do produto
  pyautogui.press('tab')
  pyautogui.write(str(base.loc[linha, 'custo']))
    #OBS do produto
  pyautogui.press('tab')
  obs = base.loc[linha, "obs"]
  if not pd.isna(obs):
    pyautogui.write(str(base.loc[linha, "obs"]))
    #Cadastrar  
  pyautogui.press('tab')
  pyautogui.press('enter')
  
# Passo 4 Repetir o processo até a ultima linha da planilha
