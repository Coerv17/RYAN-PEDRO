from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
import sqlite3
from tkinter import messagebox
from view import *
from tkinter import filedialog

# from view import atualizar_formu
################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# janela ###############

janela = Tk()
janela.title('')
janela.geometry('1170x410')
janela.iconbitmap("logo.ico")
janela.configure(background=co9)
janela.resizable(False,False)
style = ttk.Style(janela)
style.theme_use("clam")

################# FRAMES ###############

frame_cima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0)

frame_Meio = Frame(janela, width=1043, height=303, bg=co1,pady=20, relief="flat")
frame_Meio.grid(row=1, column=0, padx=1, pady=0,sticky=NSEW)

frame_Baixo = Frame(janela, width=1043, height=7000, bg=co1, relief="flat")
frame_Baixo.grid(row=2, column=0, padx=1, pady=0,sticky=NSEW)

################# CRIANDO FUNCOES ###############
global tree
###############
def inserir():
    DTREGISTRO = e_registro.get_date() # e aki tu colocou .get_data() que no caso é -----> .get_date()
    NUMBONUS = e_bonus.get()
    DTENTRADA = e_entrada.get_date()
    NUMNOTAENT = e_num.get()
    NUMLOTE = e_lote.get()
    CODPROD = e_cod.get()
    FABRICANTE = e_fabricante.get()
    DTFABRICACAO = e_dtfabi.get_date()
    DTVALIDADE = e_dtvali.get_date()
    QT = e_qt.get()

    lista_inserir = [DTREGISTRO,NUMBONUS,DTENTRADA,NUMNOTAENT,NUMLOTE,CODPROD,FABRICANTE,DTFABRICACAO,DTVALIDADE,QT]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro','Preencha todos os campos')
            return
    inserir_form(lista_inserir) # aki tava errado, chamando a função errada

    messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')
    mostar()
    
    e_registro.delete(0,'end')
    e_bonus.delete(0,'end')
    e_entrada.delete(0,'end')
    e_num.delete(0,'end')
    e_lote.delete(0,'end')
    e_cod.delete(0,'end')
    e_fabricante.delete(0,'end')
    e_dtfabi.delete(0,'end')
    e_dtvali.delete(0,'end')
    e_qt.delete(0,'end')
    

                    
#FUNCAO DELETAR 
def atializar():
    try:
        treev_dados = tree.focus()
        treev_dic = tree.item(treev_dados)
        trev_lista = treev_dic['values']

        valor = trev_lista[0]

        e_registro.delete(0,'end')
        e_bonus.delete(0,'end')
        e_entrada.delete(0,'end')
        e_num.delete(0,'end')
        e_lote.delete(0,'end')
        e_cod.delete(0,'end')
        e_fabricante.delete(0,'end')
        e_dtfabi.delete(0,'end')
        e_dtvali.delete(0,'end')
        e_qt.delete(0,'end')

        
        e_registro.insert(0,trev_lista[0]) 
        e_bonus.insert(0,trev_lista[1])
        e_entrada.insert(0,trev_lista[2])
        e_num.insert(0,trev_lista[3])
        e_lote.insert(0,trev_lista[4])
        e_cod.insert(0,trev_lista[5])
        e_fabricante.insert(0,trev_lista[6])
        e_dtfabi.insert(0,trev_lista[7])
        e_dtvali.insert(0,trev_lista[8])
        e_qt.insert(0,trev_lista[9])
        ID = int(trev_lista[10])

        def update():
            # global
            DTREGISTRO = e_registro.get_date() # e aki tu colocou .get_data() que no caso é -----> .get_date()
            NUMBONUS = e_bonus.get()
            DTENTRADA = e_entrada.get_date()
            NUMNOTAENT = e_num.get()
            NUMLOTE = e_lote.get()
            CODPROD = e_cod.get()
            FABRICANTE = e_fabricante.get()
            DTFABRICACAO = e_dtfabi.get_date()
            DTVALIDADE = e_dtvali.get_date()
            QT = e_qt.get()
            lista_atualizar = [DTREGISTRO,NUMBONUS,DTENTRADA,NUMNOTAENT,NUMLOTE,CODPROD,FABRICANTE,DTFABRICACAO,DTVALIDADE,QT,str(ID)]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro','Preencha todos os campos')
                    return
            atualizar_formu(lista_atualizar)
            messagebox.showinfo('Sucesso','Os dados foram atualizado com sucesso')
            
            e_registro.delete(0,'end')
            e_bonus.delete(0,'end')
            e_entrada.delete(0,'end')
            e_num.delete(0,'end')
            e_lote.delete(0,'end')
            e_cod.delete(0,'end')
            e_fabricante.delete(0,'end')
            e_dtfabi.delete(0,'end')
            e_dtvali.delete(0,'end')
            e_qt.delete(0,'end')


            b_confirmar.destroy()
            mostar()
            
        
        
        b_confirmar = Button(frame_Meio, image=img_delete,command=update, width=95, text='confirmar'.upper(), overrelief=RIDGE,font=('Ivy 10 bold'),bg=co1, fg=co4) 
        b_confirmar.grid(row=4, column=3, padx=0, pady=0)       

    except IndexError:
        messagebox.showerror('Erro','Seleciona um dados da tabela')


    
# def deletar3():
#     try:
#         treev_dados = tree.focus()
#         treev_dicionario = tree.item(treev_dados)
#         treev_lista = treev_dicionario['values']
#         valor = treev_lista[0]
        
        
#         deletar_formu([valor])
        
#         messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')

#         mostar()

#     except IndexError:
#         messagebox.showerror('Erro','Seleciona um dos dados na tabela')


  


################# IMAGEM ###############
app_img = Image.open('inv.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text="AAAAAAAAAAAAAA", width=1240, compound=LEFT,relief=RAISED, anchor=NW,font=('Verdana 20 bold'),bg=co1,fg=co4)
app_logo.grid(row=1, column=1, padx=1, pady=0)

################# ENTRADAS DE DADOS  ###############

l_registro = Label(frame_Meio,text='DTREGISTRO * ', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_registro.grid(row=1, column=1, padx=1, pady=0)
e_registro= DateEntry(frame_Meio, width=12, background='darkblue',bordewidth=2, year=2023)
e_registro.grid(row=2, column=1, padx=1, pady=0)


l_bonus = Label(frame_Meio,text='NUMBONUS *', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_bonus.grid(row=1, column=2, padx=2, pady=0)
e_bonus= Entry(frame_Meio, width=16, justify='left', relief=SOLID)
e_bonus.grid(row=2, column=2, padx=2, pady=0)



l_entrada = Label(frame_Meio,text='DTENTRADA *', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_entrada.grid(row=1, column=3, padx=3, pady=0)
e_entrada= DateEntry(frame_Meio, width=12, background='darkblue',bordewidth=2, year=2023)
e_entrada.grid(row=2, column=3, padx=3, pady=0)


l_num = Label(frame_Meio,text='NUMNOTAENT*', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_num.grid(row=1, column=4, padx=4, pady=0)
e_num= Entry(frame_Meio, width=16, justify='left', relief=SOLID)
e_num.grid(row=2, column=4, padx=4, pady=0)


l_lote = Label(frame_Meio,text='NUMLOTE*', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_lote.grid(row=1, column=5, padx=5, pady=0)
e_lote= Entry(frame_Meio, width=16, justify='left', relief=SOLID)
e_lote.grid(row=2, column=5, padx=5, pady=0)

l_cod = Label(frame_Meio,text='CODPROD *', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cod.grid(row=1, column=6, padx=6, pady=0)
e_cod= Entry(frame_Meio, width=16, justify='left', relief=SOLID)
e_cod.grid(row=2, column=6, padx=6, pady=0)

l_fabricante = Label(frame_Meio,text='FABRICANTE *', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_fabricante.grid(row=1, column=7, padx=7, pady=0)
e_fabricante= Entry(frame_Meio, width=16, justify='left', relief=SOLID)
e_fabricante.grid(row=2, column=7, padx=7, pady=0)

l_dtfabri = Label(frame_Meio,text='DTFABRICACAO *', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_dtfabri.grid(row=1, column=8, padx=8, pady=0)
e_dtfabi= DateEntry(frame_Meio, width=12, background='darkblue',bordewidth=2, year=2023)
e_dtfabi.grid(row=2, column=8, padx=7, pady=0)

l_dtvali = Label(frame_Meio,text='DTVALIDADE *', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_dtvali.grid(row=1, column=9, padx=9, pady=0)
e_dtvali= DateEntry(frame_Meio, width=12, background='darkblue',bordewidth=2, year=2023)
e_dtvali.grid(row=2, column=9, padx=9, pady=1)

l_qt = Label(frame_Meio,text='QT *', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
l_qt.grid(row=1, column=10, padx=10, pady=0)
e_qt= Entry(frame_Meio, width=16, justify='left', relief=SOLID)
e_qt.grid(row=2, column=10, padx=10, pady=0)


################# BOTOES  ###############
img_add = Image.open('adicionar.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
adicinocar = Button(frame_Meio, command=inserir, image=img_add, width=95, text='Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 10 bold'),bg=co1, fg=co4) 
adicinocar.grid(row=4, column=1, padx=0, pady=0)

img_delete = Image.open('botao-atualizar.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

deletar = Button(frame_Meio, image=img_delete,command=atializar, width=95, text='Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 10 bold'),bg=co1, fg=co4) 
deletar.grid(row=4, column=2, padx=0, pady=0)



img_deletar = Image.open('bloquear.png')
img_deletar = img_deletar.resize((20,20))
img_deletar = ImageTk.PhotoImage(img_deletar)

# deletar = Button(frame_Meio, image=img_deletar, command=deletar3,width=95, text='Deletar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 10 bold'),bg=co1, fg=co4) 
# deletar.grid(row=4, column=3, padx=0, pady=0)



################################################
def mostar():
    global tree
    tabela_head = ['IDTREGISTRO'.upper(),'NUMBONUS'.upper(),  'DTENTRADA'.upper(),'NUMNOTAENT'.upper(), 'NUMLOTE'.upper(), 'CODPROD'.upper(),'FABRICANTE'.upper(), 'DTFABRICACAO'.upper(),'DTVALIDADE'.upper(),'QT'.upper()]

    lista_itens = ver_formu()



    tree = ttk.Treeview(frame_Baixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_Baixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_Baixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_Baixo.grid_rowconfigure(0, weight=120)

    hd=["center","center","center","center","center","center","center", 'center','center','center']
    h=[100,150,100,160,130,100,100, 100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.upper(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = [8888,88]

    # for iten in lista_itens:
    #     quantidade.append(iten[6])

    # Total_valor = sum(quantidade)
    # Total_itens = len(quantidade)

    # # l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    # # l_qtd['text'] = Total_itens




    # l_nomea = Label(frame_Meio,text='nome * ', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
    # l_nomea.place(x=10, y= 40)
    # e_nomea= Entry(frame_Meio, width=30, justify='left', relief=SOLID)
    # e_nomea.place(x=130,y=41)


    # l_nomea = Label(frame_Meio,text='nome * ', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
    # l_nomea.place(x=10, y= 70)
    # e_nomea= Entry(frame_Meio, width=30, justify='left', relief=SOLID)
    # e_nomea.place(x=130,y=71)


    # l_nomea = Label(frame_Meio,text='nome * ', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
    # l_nomea.place(x=10, y= 100)
    # e_nomea= Entry(frame_Meio, width=30, justify='left', relief=SOLID)
    # e_nomea.place(x=130,y=101)

mostar()





janela.mainloop()


