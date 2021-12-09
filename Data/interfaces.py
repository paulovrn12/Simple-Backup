# Importações:
from tkinter import *

def CentroMonitor(janela_master, largura_janela, altura_janela):
    # DIMENSÕES DO MONITOR
    larg_monitor = janela_master.winfo_screenwidth()
    altu_monitor = janela_master.winfo_screenheight()
    # CALCULOS DE CENTRALIZAÇÃO
    posi_largura = (larg_monitor / 2) - (largura_janela / 2)
    posi_altura = (altu_monitor / 2) - (altura_janela / 2)
    # CONVERSÃO INT PARA STR
    largura_janela = str(int(largura_janela))
    altura_janela = str(int(altura_janela))
    posi_largura = str(int(posi_largura))
    posi_altura = str(int(posi_altura))
    return janela_master.geometry(f'{largura_janela}x{altura_janela}+{posi_largura}+{posi_altura}')

# TELA INICIAL:
def TelaInicial():
    # início da janela
    janela = Tk()
    # características da janela
    janela.title('Simple Backup v0.1')
    CentroMonitor(janela, 600, 400)
    janela.iconbitmap(r'Simple Backup\Icons\paste.ico')
    janela.resizable(False, False)
    # frames
    topo = Frame(janela, bg='#999999', width=600, height=100)
    meio = Frame(janela, bg='#e6e6e6', width=600, height=250)
    rodapé = Frame(janela, bg='#333333', width=600, height=50)
    # widgets da janela
    texto = Label(topo, text='Olá mundo!')
    # layouts da janela
    topo.grid(sticky='nsew')
    texto.pack()
    meio.grid(sticky='nsew')
    rodapé.grid(sticky='nsew')
    # fim da janela
    janela.mainloop()

# TELA DE BACKUP RÁPIDO:

# TELA DE BACKUP AVANÇADO:

# TELA DE SELEÇÃO DE DIRETÓRIOS:

TelaInicial()
