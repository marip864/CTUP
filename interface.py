import tkinter as tk
from PIL import Image, ImageTk  # Necessário para imagens em formatos como PNG ou JPG

# Função para capturar o valor digitado

def capturar_dados():
    pressao = entrada_pressao.get()
    temperatura = entrada_temperatura.get()
    # Aqui você pode converter para float, se necessário
    try:
        pressao = float(pressao)
        temperatura = float(temperatura)
        print(f"Pressão: {pressao} atm")
        print(f"Temperatura: {temperatura} K")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


# Configuração da janela principal
janela = tk.Tk()
janela.title("Exemplo de Entry no Tkinter")

# Carregar a imagem (usando PIL para maior compatibilidade)
imagem = Image.open("images/Logo_CTUP-removebg-preview.png")  # Substitua pelo caminho da sua imagem
imagem_tk = ImageTk.PhotoImage(imagem)

# Adicionar a imagem em um Label
label_imagem = tk.Label(janela, image=imagem_tk)
label_imagem.pack()

# Label de instrução
label_pressao = tk.Label(janela, text="Digite a pressão (em atm):")
label_pressao.pack(pady=5)

# Caixa de texto (Entry)
entrada_pressao = tk.Entry(janela, width=30)
entrada_pressao.pack(pady=5)

# Label de instrução
label_temperatura = tk.Label(janela, text="Digite a temperatura (em K):")
label_temperatura.pack(pady=5)

# Caixa de texto (Entry)
entrada_temperatura = tk.Entry(janela, width=30)
entrada_temperatura.pack(pady=5)

# Botão para capturar o valor
botao = tk.Button(
    janela,
    text="Clique Aqui",
    font=("Arial", 14, "bold"), # Fonte, tamanho e estilo
    bg="darkblue",             # Cor de fundo
    fg="white",                 # Cor do texto
    activebackground="blue",    # Cor de fundo ao clicar
    activeforeground="yellow",  # Cor do texto ao clicar
    relief="raised",            # Estilo da borda (raised, sunken, flat, etc.)
    bd=5,                       # Largura da borda
    command=capturar_dados
)
botao.pack(pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5)

# Inicia o loop da interface
janela.mainloop()
