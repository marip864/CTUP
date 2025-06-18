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


    

# Configuração da janela principal
janelaPrincipal = tk.Tk()
janelaPrincipal.title("Seja bem-vindo ao CTUP!")
janelaPrincipal.geometry("400x800")

# Carrega a imagem (usando PIL para maior compatibilidade)
imagem = Image.open("images/Logo_CTUP-removebg-preview.png") 
imagem_tk = ImageTk.PhotoImage(imagem)

# Adiciona a imagem em um Label
label_imagem = tk.Label(janelaPrincipal, image=imagem_tk)
label_imagem.pack()

# Label da pressão inicial
label_pressao1 = tk.Label(janelaPrincipal, text="Digite a pressão inicial (em Pa):")
label_pressao1.pack(pady=5)

# Caixa de texto para pressão inicial (Entry)
entrada_pressao1 = tk.Entry(janelaPrincipal, width=30)
entrada_pressao1.pack(pady=5)

# Label da temperatura inicial
label_temperatura1 = tk.Label(janelaPrincipal, text="Digite a temperatura inicial (em K):")
label_temperatura1.pack(pady=5)

# Caixa de texto para temperatura inicial (Entry)
entrada_temperatura1 = tk.Entry(janelaPrincipal, width=30)
entrada_temperatura1.pack(pady=5)

# Label do volume inicial
label_volume1 = tk.Label(janelaPrincipal, text="Digite o volume inicial (em l):")
label_volume1.pack(pady=5)

# Caixa de texto para temperatura inicial (Entry)
entrada_volume1 = tk.Entry(janelaPrincipal, width=30)
entrada_volume1.pack(pady=5)

# Label da pressão inicial
label_pressao2 = tk.Label(janelaPrincipal, text="Digite a pressão inicial (em Pa):")
label_pressao2.pack(pady=5)

# Caixa de texto para pressão inicial (Entry)
entrada_pressao2 = tk.Entry(janelaPrincipal, width=30)
entrada_pressao2.pack(pady=5)

# Label da temperatura inicial
label_temperatura2 = tk.Label(janelaPrincipal, text="Digite a temperatura inicial (em K):")
label_temperatura2.pack(pady=5)

# Caixa de texto para temperatura inicial (Entry)
entrada_temperatura2 = tk.Entry(janelaPrincipal, width=30)
entrada_temperatura2.pack(pady=5)

# Label do volume inicial
label_volume2 = tk.Label(janelaPrincipal, text="Digite o volume inicial (em l):")
label_volume2.pack(pady=5)

# Caixa de texto para temperatura inicial (Entry)
entrada_volume2 = tk.Entry(janelaPrincipal, width=30)
entrada_volume2.pack(pady=5)

# Botão para capturar os valores
botao = tk.Button(
    janelaPrincipal,
    text="Clique Aqui",
    font=("Arial", 14, "bold"), # Fonte, tamanho e estilo
    bg="darkblue",             # Cor de fundo
    fg="white",                 # Cor do texto
    relief="raised",            # Estilo da borda (raised, sunken, flat, etc.)
    bd=5,                       # Largura da borda
    command=parametrosNovaJanela
)
botao.pack(pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(janelaPrincipal, text="")
label_resultado.pack(pady=5)

# Inicia o loop da interface
janelaPrincipal.mainloop()
