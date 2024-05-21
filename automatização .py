import pyautogui as pg
import time

pg.PAUSE = 0.5

# passo a passo:
# Abrir o link
pg.press ("win")
pg.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(0.5)
pg.press ("enter")
time.sleep (2)

# fazer login
    #Point(x=1049, y=360) email

pg.click (x=1049, y=360)
pg.write ("emaildofabinho@email.com")
pg.press("tab")

pg.write ("senha.senha")
pg.press("enter")


# abrir base de dados a ser cadatrada
import pandas as pd

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    # cadastrar itens no sistema
        #Point(x=951, y=236) ("código do produto")
    cdg =str (tabela.loc[linha, "codigo"])

        #preencher o código do protuto
    pg.click(x=951, y=236)
    pg.write(cdg)
    pg.press("tab")

        #marca
    
    pg.write(str (tabela.loc [linha, "marca"]))
    pg.press("tab")

        #tipo
    
    pg.write(str (tabela.loc [linha, "tipo"]))
    pg.press("tab")

        #categoria
    pg.write(str (tabela.loc [linha, "categoria"]))
    pg.press("tab")

        #preço
    pg.write(str (tabela.loc [linha, "preco_unitario"]))
    pg.press("tab")

        #custo
    pg.write(str (tabela.loc [linha, "custo"]))
    pg.press("tab")

        #obs (para este campo que contem células vazias iremos retirar o preencimento automático)

    obs = str (tabela.loc [linha, "obs"])
    if obs != "nan":
        pg.write(obs)
    pg.press("tab")

        #apertar botão e voltar ao inicio
    pg.press("enter")
    pg.scroll(10000)


# repetir processos
