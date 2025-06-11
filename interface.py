import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necessário para imagens em formatos como PNG ou JPG

# Função para capturar o valor digitado
def capturar_dados():
    pressao = entrada_pressao.get()
    temperatura = entrada_temperatura.get()
    # Conversão para float
    try:
        pressao = float(pressao)
        temperatura = float(temperatura)
        print(f"Pressão: {pressao} atm")
        print(f"Temperatura: {temperatura} K")
        abrirJanela(pressao, temperatura)
    except ValueError:
        janelaPrincipal.withdraw()  
        # Mostrar a message box
        messagebox.showinfo("Information", "Por favor, insira valores numéricos!")
        print("Por favor, insira valores numéricos válidos.")

def abrirJanela(p, t):
    novaJanela = tk.Toplevel()
    novaJanela.title("Gráficos")
    novaJanela.geometry("400x400")
    tk.Label(novaJanela, text=f"Dados recebidos: {p} e {t}").pack(pady=20)
    tk.Button(novaJanela, text="Fechar", command=novaJanela.destroy).pack()
    

# Configuração da janela principal
janelaPrincipal = tk.Tk()
janelaPrincipal.title("Seja bem-vindo ao CTUP!")
janelaPrincipal.geometry("400x400")

# Carrega a imagem (usando PIL para maior compatibilidade)
imagem = Image.open("images/Logo_CTUP-removebg-preview.png") 
imagem_tk = ImageTk.PhotoImage(imagem)

# Adiciona a imagem em um Label
label_imagem = tk.Label(janelaPrincipal, image=imagem_tk)
label_imagem.pack()

# Label da pressão
label_pressao = tk.Label(janelaPrincipal, text="Digite a pressão (em Pa):")
label_pressao.pack(pady=5)

# Caixa de texto para pressão (Entry)
entrada_pressao = tk.Entry(janelaPrincipal, width=30)
entrada_pressao.pack(pady=5)

# Label da temperatura
label_temperatura = tk.Label(janelaPrincipal, text="Digite a temperatura (em K):")
label_temperatura.pack(pady=5)

# Caixa de texto para temperatura (Entry)
entrada_temperatura = tk.Entry(janelaPrincipal, width=30)
entrada_temperatura.pack(pady=5)

# Botão para capturar os valores
botao = tk.Button(
    janelaPrincipal,
    text="Clique Aqui",
    font=("Arial", 14, "bold"), # Fonte, tamanho e estilo
    bg="darkblue",             # Cor de fundo
    fg="white",                 # Cor do texto
    relief="raised",            # Estilo da borda (raised, sunken, flat, etc.)
    bd=5,                       # Largura da borda
    command=capturar_dados
)
botao.pack(pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(janelaPrincipal, text="")
label_resultado.pack(pady=5)

# Inicia o loop da interface
janelaPrincipal.mainloop()
