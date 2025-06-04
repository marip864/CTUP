import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Interface Gráfica")
janela.geometry("300x200")

# Adicionando um rótulo
rotulo = tk.Label(janela, text="Bem-vindo à interface gráfica!", font=("Arial", 12))
rotulo.pack(pady=10)

# Adicionando um botão
def clique_botao():
    rotulo.config(text="Você clicou no botão!")

botao = tk.Button(janela, text="Clique aqui", command=clique_botao)
botao.pack(pady=10)

# Executando o loop principal
janela.mainloop()