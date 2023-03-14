import pandas as pd
import tkinter as tk
import sqlite3

# Conectar ao banco de dados SQLite3
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criar a tabela no banco de dados SQLite3
cursor.execute('''CREATE TABLE IF NOT EXISTS estoque
                  (id INTEGER PRIMARY KEY,
                   nome TEXT,
                   data_validade DATE,
                   estoque INTEGER)''')
conn.commit()

# Carregar a tabela do banco de dados para um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM estoque", conn)

# Definir função para diminuir o estoque
def diminuir_estoque():
    # Obter o ID do produto e a quantidade a ser removida a partir das caixas de entrada
    produto_id = int(produto_id_entry.get())
    quantidade = int(quantidade_entry.get())

    # Encontrar a linha correspondente ao produto com a menor data de validade
    produto = df.loc[df['id'] == produto_id]
    menor_data_validade_idx = produto.groupby('id')['data_validade'].idxmin()
    linha = produto.loc[menor_data_validade_idx]

    # Subtrair a quantidade desejada do estoque na linha correspondente
    estoque_atual = linha['estoque'].values[0]
    novo_estoque = estoque_atual - quantidade
    df.at[linha.index[0], 'estoque'] = novo_estoque

    # Atualizar o banco de dados SQLite3 com os novos valores
    cursor.execute("UPDATE estoque SET estoque = ? WHERE id = ? AND data_validade = ?", (novo_estoque, produto_id, linha['data_validade'].values[0]))
    conn.commit()

    # Limpar as caixas de entrada
    produto_id_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)

# Criação da janela principal
root = tk.Tk()
root.title("Diminuir estoque")

# Criação de caixas de entrada para o ID do produto e quantidade a ser removida
produto_id_label = tk.Label(root, text="ID do produto:")
produto_id_label.pack()
produto_id_entry = tk.Entry(root)
produto_id_entry.pack()

quantidade_label = tk.Label(root, text="Quantidade a ser removida:")
quantidade_label.pack()
quantidade_entry = tk.Entry(root)
quantidade_entry.pack()

# Criação do botão para diminuir o estoque
diminuir_estoque_button = tk.Button(root, text="Diminuir estoque", command=diminuir_estoque)
diminuir_estoque_button.pack()

# Executar o loop principal do tkinter
root.mainloop()
