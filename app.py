import tkinter as tk
import sqlite3
from tkinter import messagebox
from main import *

conn = sqlite3.connect('formu.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXTN NOT NULL,
              senha TEXT NOT NULL)''')
class TelaLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Login AAA')
        

        self.label_nome = tk.Label(self, text='Nome:')
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=0, column=1)

        self.label_senha = tk.Label(self, text='Senha:')
        self.label_senha.grid(row=1, column=0)

        self.entry_senha = tk.Entry(self, show='*')
        self.entry_senha.grid(row=1, column=1)

        self.button_login = tk.Button(self, text='Login',  command=lambda: [self.login()])
        self.button_login.grid(row=2, column=0)

        self.button_cadastrar = tk.Button(self, text='Cadastrar', command=self.abrir_tela_cadastro)
        self.button_cadastrar.grid(row=2, column=1)
        

    def login(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

        c.execute('''SELECT * FROM usuarios WHERE nome = ? AND senha = ?''', (nome, senha))
        resultado = c.fetchone()

        if resultado is not None:
            print('Login realizado com sucesso!')
            tela_cadastro = janela()
            tela_cadastro.mainloop()
        else:
            print('Nome de usuário ou senha incorretos.')

    def abrir_tela_cadastro(self):
        tela_cadastro = TelaCadastro()
        tela_cadastro.mainloop()
    
    def abrir_tela_for(self):
        tela_cadastro = Telafor()
        tela_cadastro.mainloop()
    


class TelaCadastro(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Cadastro')

        self.label_nome = tk.Label(self, text='Nome:')
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=0, column=1)

        self.label_senha = tk.Label(self, text='Senha:')
        self.label_senha.grid(row=1, column=0)

        self.entry_senha = tk.Entry(self, show='*')
        self.entry_senha.grid(row=1, column=1)

        self.button_cadastrar = tk.Button(self, text='Cadastrar', command=self.cadastrar)
        self.button_cadastrar.grid(row=2, column=0)

        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.destroy)
        self.button_cancelar.grid(row=2, column=1)

    def cadastrar(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

        c.execute('''INSERT INTO usuarios (nome, senha) VALUES (?, ?)''', (nome, senha))
        conn.commit()

        messagebox.showinfo("Título da mensagem", "Esta é uma mensagem informativa.")
        self.destroy()

    

class Telafor(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Cadastro')

        self.label_nome = tk.Label(self, text='TESTE:')
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=0, column=1)

        self.label_senha = tk.Label(self, text='Senha:')
        self.label_senha.grid(row=1, column=0)

        self.entry_senha = tk.Entry(self, show='*')
        self.entry_senha.grid(row=1, column=1)

        




if __name__ == '__main__':
    tela_login = TelaLogin()
    tela_login.mainloop()

conn.close()
