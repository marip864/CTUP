import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Necessário para imagens em formatos como PNG ou JPG
from calculos import calculadora

# Função para capturar o valor digitado
def capturar_dados():
    pressao1 = entrada_pressao1.get()
    temperatura1 = entrada_temperatura1.get()
    volume1 = entrada_volume1.get()
    pressao2 = entrada_pressao2.get()
    temperatura2 = entrada_temperatura2.get()
    volume2 = entrada_volume2.get()
    # Conversão para float
    try:
        pressao1 = float(pressao1)
        temperatura1 = float(temperatura1)
        volume1 = float(volume1)
        pressao2 = float(pressao2)
        temperatura2 = float(temperatura2)
        volume2 = float(volume2)
        print(f"Pressão inicial: {pressao1} atm")
        print(f"Temperatura inicial: {temperatura1} K")
        print(f"Volume inicial: {volume1} litros")
        print(f"Pressão: {pressao2} atm")
        print(f"Temperatura: {temperatura2} K")
        print(f"Volume: {volume2} litros")
        return pressao1, volume1, temperatura1, pressao2, volume2, temperatura2
    except ValueError:
        janelaPrincipal.withdraw()  
        # Mostrar a message box
        messagebox.showinfo("Information", "Por favor, insira valores numéricos!")
        print("Por favor, insira valores numéricos válidos.")
        janelaPrincipal.deiconify()

def parametrosNovaJanela():
    pressao1, volume1, temperatura1, pressao2, volume2, temperatura2 = capturar_dados()
    try:
        abrirJanela(pressao1, temperatura1, volume1, pressao2, volume2, temperatura2)
    except ValueError:
        janelaPrincipal.withdraw()  
        # Mostrar a message box
        messagebox.showinfo("Information", "Por favor, insira valores numéricos!")
        print("Por favor, insira valores numéricos válidos.")

def abrirJanela(p1, t1, v1, p2, t2, v2):
    novaJanela = tk.Toplevel()
    novaJanela.title("Resultados do Ciclo Termodinâmico")
    novaJanela.geometry("1000x400")
    tk.Label(novaJanela, text=f"Dados recebidos: {p1} e {t1} e {v1}").pack(pady=20)

    resultado = calculadora(p1, t1, v1, p2, t2, v2)

    cols = ("Q", "W", "ΔU", "ΔS")
    tree = ttk.Treeview(novaJanela, columns=cols, show='headings')

    for col in cols:
        tree.heading(col, text=col)

    for transformacao in resultado[:-2]:
        tree.insert("", "end", values=transformacao)

    
    totais = resultado[-2]
    tree.insert("", "end", values=("Totais", "", "", ""))
    tree.insert("", "end", values=totais)

    rendimento = resultado[-1]
    tree.insert("", "end", values=("Rendimento", rendimento, "", "", ""))

    tree.pack()

    tk.Button(novaJanela, text="Fechar", command=novaJanela.destroy).pack()



# Janela principal
janelaPrincipal = tk.Tk()
janelaPrincipal.title("Seja bem-vindo ao CTUP!")
janelaPrincipal.geometry("400x700")
janelaPrincipal.configure(bg="#f0f0f0")

# Imagem
imagem = Image.open("images/Logo_CTUP-removebg-preview.png")
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janelaPrincipal, image=imagem_tk, bg="#f0f0f0")
label_imagem.pack(pady=10)


# Estilo padrão
label_style = {"font": ("Arial", 10), "bg": "#f0f0f0", "fg": "#333"}

# Função para criar campos
def criar_campo(label_texto, entrada_var):
    label = tk.Label(janelaPrincipal, text=label_texto, **label_style)
    label.pack(pady=5)
    entrada = tk.Entry(janelaPrincipal, width=30, textvariable=entrada_var)
    entrada.pack(pady=5)
    return entrada

# Variáveis e campos
p1 = tk.StringVar()
t1 = tk.StringVar()
v1 = tk.StringVar()
p2 = tk.StringVar()
t2 = tk.StringVar()
v2 = tk.StringVar()

entrada_pressao1 = criar_campo("Digite a pressão inicial (em Pa):", p1)
entrada_temperatura1 = criar_campo("Digite a temperatura inicial (em K):", t1)
entrada_volume1 = criar_campo("Digite o volume inicial (em m³):", v1)
entrada_pressao2 = criar_campo("Digite a pressão final (em Pa):", p2)
entrada_temperatura2 = criar_campo("Digite a temperatura final (em K):", t2)
entrada_volume2 = criar_campo("Digite o volume final (em m³):", v2)


botao = tk.Button(
    janelaPrincipal,
    text="Clique Aqui",
    font=("Arial", 12, "bold"),
    bg="darkblue",
    fg="white",
    relief="raised",
    bd=5,
    command=parametrosNovaJanela
)
botao.pack(pady=20)


# Resultado
label_resultado = tk.Label(janelaPrincipal, text="", **label_style)
label_resultado.pack(pady=5)

# Loop
janelaPrincipal.mainloop()



