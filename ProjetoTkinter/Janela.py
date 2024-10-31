from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pyodbc

# Primeiro estabeleci a conexão com o banco de dados:

dados_conexao = (r"Driver={SQL Server};"
                 r"Server={server};"
                 r"Database={database}")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#Criei uma função para cada botão:

def btn_clicked0():
    # Pegar a informação de todos os campos (entry0, entry1, entry2 e entry3);
    nome_produto = entry0.get()
    data_validade = entry1.get()
    lote = entry2.get()
    quantidade = entry3.get()

    # preencher o banco de dados de acordo com essa informações;
    comando = f"""INSERT INTO Insumos(nome_produto, data_validade, lote, quantidade)
            VALUES('{nome_produto}', '{data_validade}', '{lote}', '{quantidade}')"""
    
    cursor.execute(comando)
    cursor.commit()

    # Exibir uma mensagem informando que o produto foi adicionado com sucesso; e
    tkinter.messagebox.showinfo(title= "Aviso sobre produto adicionado" , message= "Produto adicionado com sucesso!")
    
    #Limpas os campos preenchidos.
    nome_produto = entry0.delete(0, tk.END)
    data_validade = entry1.delete(0, tk.END)
    lote = entry2.delete(0, tk.END)
    quantidade = entry3.delete(0, tk.END)


def btn_clicked1():
    # Pegar a informação dos campos "Nome" (entry0) e "Quantidade" (entry3); 
    nome_produto = entry0.get()
    quantidade_utilizada = entry3.get()

    # buscar o insumo pelo nome dele no banco de dados; 
    # diminuir a quantidade informada no banco dados, de acordo com a quantidade preenchida;
    comando = f"""UPDATE Insumos
            SET quantidade = quantidade - {quantidade_utilizada}
            WHERE nome_produto = '{nome_produto}';"""
    cursor.execute(comando)
    cursor.commit()
    

    # Exibir uma mensagem informando a quantidade utilizada do produto; e
    tkinter.messagebox.showinfo(title= "Aviso de utilização de produto" , message= f"{quantidade_utilizada} unidade(s) do Produto {nome_produto} utilizada(s)!")

    #Limpas os campos preenchidos.
    nome_produto = entry0.delete(0, tk.END)
    quantidade_utilizada = entry3.delete(0, tk.END)


def btn_clicked2():
    # Pegar a informação preenchida no campo "Nome" (entry0);
    nome_produto = entry0.get()

    # buscar correspondência no banco de dados para essa informação;
    comando = f"""SELECT * from Insumos
            WHERE nome_produto = '{nome_produto}';"""
    cursor.execute(comando)

    # colocar as correspondências obtidas na caixa de texto (entry4); e
    linha_tracejada = "".join(["-" for _ in range(21)])
    for linha in cursor.fetchall():
        texto = f"Item: {linha.nome_produto};\nQuantidade: {linha.quantidade}; \nLote:{linha.lote}; \nValidade:{linha.data_validade}\n{linha_tracejada}\n"
        entry4.insert('1.0', texto, END)

    #Limpas os campos preenchidos.
    nome_produto = entry0.delete(0, tk.END)


def btn_clicked3():
    # Pegar a informação preenchida no campo "Nome" (entry0);
    nome_produto = entry0.get()
    # deletar do banco de dados o insumo com o nome inserido;
    comando = f"""DELETE from insumos
            WHERE nome_produto = '{nome_produto}';"""
    
    cursor.execute(comando)
    cursor.commit()
    # Exibir uma mensagem informando que o produtor foi deletado com sucesso; e
    tkinter.messagebox.showinfo(title= "Aviso de exclusão de produto" , message= f"Produto {nome_produto} foi excluído com sucesso!")
    
    #Limpas os campos preenchidos.
    nome_produto = entry0.delete(0, tk.END)

# montei a interface da janela do programa no Figma e importei o código pelo Proxlight Designer.
# Feito isso, precisei descobrir qual parte do código dizia respeito a cada botão/campo de texto.
# print(entry0.get()) -> Nome
# print(entry1.get()) -> Data de Validade
# print(entry2.get()) -> Lota
# print(entry3.get()) -> Quantidade
# entry4.get(1.0, END) -> Exibe infos do produto do banco de dados

window = Tk()

window.geometry("700x650")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 650,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    350.0, 313.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 126, y = 106,
    width = 210,
    height = 53)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 363, y = 106,
    width = 210,
    height = 53)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 363, y = 179,
    width = 210,
    height = 53)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b3.place(
    x = 127, y = 179,
    width = 210,
    height = 53)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    320.0, 298.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 200, y = 283,
    width = 240,
    height = 28)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    320.0, 340.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 200, y = 325,
    width = 240,
    height = 28)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    320.0, 382.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 200, y = 367,
    width = 240,
    height = 28)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    320.0, 424.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 200, y = 409,
    width = 240,
    height = 28)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    244.5, 542.0,
    image = entry4_img)

entry4 = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry4.place(
    x = 49, y = 469,
    width = 391,
    height = 144)

window.resizable(False, False)

window.mainloop()
