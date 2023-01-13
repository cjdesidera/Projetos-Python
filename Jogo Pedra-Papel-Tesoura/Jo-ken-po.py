import tkinter
from tkinter import *
from tkinter import ttk, Button, Text, filedialog
import random

# CORES
fundo = '#404040'
cor1 = '#FFFAFA' #branquinho neve
cor2 = "#fcc058"  # orange / laranja
cor3 = "#fff873"  # yellow / amarela
cor4 = "#34eb3d"   # green / verde
cor5 = "#e85151"   # red / vermelha

# CONFIGURAÇÃO DA JANELA
janela =Tk()
janela.title('JO-KEN-PO')
janela.geometry('300x300')
janela.configure(bg=fundo)

# DIVIDINDO A JANELA
frame_superior = Frame(janela, width=300, height=100, bg=fundo, relief='raised')
frame_superior.grid(row=0, column=0, sticky=NW)
frame_inferior = Frame(janela, width=300, height=200, bg=cor1, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# CONFIGURANDO FRAMES SUPERIOR
jog= Label(frame_superior, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), bg=fundo, fg=cor1)
jog.place(x=40, y=75)
jog_pontos= Label(frame_superior, text="0", height=1, anchor='center', font=('Ivy 40 bold'), bg=fundo, fg=cor1)
jog_pontos.place(x=65, y=10)
jog_linha= Label(frame_superior, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=cor2)
jog_linha.place(x=0, y=75)

app= Label(frame_superior, text=" : ", height=1, anchor='center', font=('Ivy 40 bold'), bg=fundo, fg=cor1)
app.place( x=125, y=10)

compu= Label(frame_superior, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=fundo, fg=cor1)
compu.place(x=230, y=75)
compu_pontos= Label(frame_superior, text="0", height=1, anchor='center', font=('Ivy 40 bold'), bg=fundo, fg=cor1)
compu_pontos.place(x=200, y=10)
compu_linha= Label(frame_superior, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=cor2)
compu_linha.place(x=295, y=75)


#FUNÇÃO DO JOGO

pontos_vc=0
pontos_pc=0
rondas=0

def jogar(i):
    global rondas
    global voce
    global pc
    global pontos_vc
    global pontos_pc

    if rondas < 5:
        print(rondas)
        opcoes =  ['Pedra','Papel','Tesoura']
        pc = random.choice(opcoes)
        vc = i
        #empate
        if vc == 'Pedra' and pc == 'Pedra':
            print('Empate')
        elif vc == 'Papel' and pc == 'Papel':
            print('Empate')
        elif vc == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
        #vitoria
        elif vc == 'Papel' and pc == 'Pedra':
            print('Ganhou')
            pontos_vc += 1
        elif vc == 'Tesoura' and pc == 'Papel':
            print('Ganhou')
            pontos_vc += 1
        elif vc == 'Pedra' and pc == 'Tesoura':
            print('Ganhou')
            pontos_vc += 1
        #derrota
        elif vc == 'Pedra' and pc == 'Papel':
            print('Perdeu')
            pontos_pc += 1
        elif vc == 'Papel' and pc == 'Tesoura':
            print('Perdeu')
            pontos_pc += 1
        else:
            print('Perdeu')
            pontos_pc += 1

        jog_pontos['text'] = pontos_vc
        compu_pontos['text']= pontos_pc
        rondas += 1

    else:
        fimJogo()


#FUNÇÃO INICIAR O JOGO
def iniciar_jogo():
    global icon1
    global icon2
    global icon3
    global b_pedra
    global b_papel
    global b_tesoura
    # criando icones
    b_jogar.destroy()

    icon1=PhotoImage(file='IMAGENS/pedra.png')
    icon1=icon1.subsample(5,5)
    b_pedra = Button(frame_inferior, command=lambda: jogar('Pedra'), text='PEDRA', width=60, image=icon1, fg=cor4, bg= cor1)
    b_pedra.place(x=20, y=50)

    icon2=PhotoImage(file='IMAGENS/papel.png')
    icon2=icon2.subsample(5,5)
    b_papel = Button(frame_inferior, command=lambda: jogar('Papel'), text='PAPEL', width=60, image=icon2, fg=cor4, bg= cor1)
    b_papel.place(x=120, y=50)

    icon3=PhotoImage(file='IMAGENS/teso.png')
    icon3=icon3.subsample(5,5)
    b_tesoura= Button(frame_inferior, command=lambda: jogar('Tesoura'), text='TESOURA', width=60, image=icon3, fg=cor4, bg= cor1)
    b_tesoura.place(x=210, y=50)

#FUNÇÃO TERMINAR JOGO
def fimJogo():
    global rondas
    global pontos_vc
    global pontos_pc

    pontos_vc=0
    pontos_pc=0
    rondas=0

    #detruir os botoes
    b_pedra.detroy()
    b_papel.destroy()
    b_tesoura.destroy()
    #definir o vencedor
    jogador_vc = int(jog_pontos['tex'])
    jogador_pc = int(compu_pontos['tex'])
    if jogador_vc > jogador_pc:
        app_vence = Label(frame_inferior, text='Parabéns! Você ganhou!', height=1, anchor=CENTER, font='Ivy 11 bold')
        app_vence.place(x=125, y=15)
    else:
        app_derrota = Label(frame_inferior, text='Perdeuuuuuuuuuuuuuuuu', height=1, anchor=CENTER, font='Ivy 11 bold')
        app_vence.place(x=125, y=15)

b_jogar = Button(frame_inferior, command=iniciar_jogo, width=30, text='JOGAR', compound=CENTER, bg=fundo, fg=cor1, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
b_jogar.place(x=20, y=150)


janela.mainloop()
