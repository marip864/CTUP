import tkinter as tk
from PIL import Image, ImageTk  # Necessário para imagens em formatos como PNG ou JPG


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
label_pressao = tk.Label(janelaPrincipal, text="Para começar, digite a quantidade de pontos que deve ser considerada:")
label_pressao.pack(pady=5)

# Caixa de texto para temperatura (Entry)
entrada_qtdPontos = tk.Entry(janelaPrincipal, width=30)
entrada_qtdPontos.pack(pady=5)

# Botão para capturar os valores
botao = tk.Button(
    janelaPrincipal,
    text="Vamos lá!",
    font=("Arial", 14, "bold"), # Fonte, tamanho e estilo
    bg="darkblue",             # Cor de fundo
    fg="white",                 # Cor do texto
    relief="raised",            # Estilo da borda (raised, sunken, flat, etc.)
    bd=5,                       # Largura da borda
    command=abrirJanela
)
botao.pack(pady=5)

# Inicia o loop da interface
janelaPrincipal.mainloop()