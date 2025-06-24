import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necessário para imagens em formatos como PNG ou JPG
from calculaNpontos import calculadora
from graficos import plotar_graficos

def capturar_dados(entries):
    # Tratamento de exceção: caso não sejam digitados valores numéricos
    try:
        dados = []
        # Conversão dos dados para float
        for entry_p, entry_v, entry_t in entries:
            pressao = float(entry_p.get())
            volume = float(entry_v.get())
            temperatura = float(entry_t.get())
            dados.append((pressao, volume, temperatura))
        return dados
    except Exception as e:
        tk.messagebox.showinfo("Erro", "Digite valores numéricos para pressão, volume e temperatura!")

def abrirJanelaResultados(dados):
    # Verificação dos dados inseridos
    if len(dados) < 2:
        tk.messagebox.showinfo("Erro", "É necessário pelo menos 2 pontos para calcular o ciclo.")
        return
    try:
        resultados = calculadora(tuple(dados))
    except Exception as e:
        tk.messagebox.showinfo("Erro", f"Erro ao calcular os resultados: {e}")
        return

    # Acessa a tupla para obter valores totais, rendimento e W, U, S das transformações
    totais = resultados[-2]
    rendimento = resultados[-1]
    transformacoes = resultados[:-2]

    # Abre nova janela para mostrar resultados calculados
    novaJanela = tk.Toplevel()
    novaJanela.title("Resultados do Ciclo Termodinâmico")
    novaJanela.geometry("900x200")

    cols = ("Transformação", "Q", "W", "ΔU", "ΔS")
    tree = ttk.Treeview(novaJanela, columns=cols, show='headings', height=10)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    # Inserir transformações
    for i, t in enumerate(transformacoes):
        tree.insert("", "end", values=(f"{i+1}", *t))
        tree.insert("", "end", values=("", "", "", "", ""))  # linha em branco para espaçamento

    # Inserir totais
    totais_formatados = (
        "Totais",
        f"{totais[2]} (Q = Qr + Qc)",
        totais[3],
        totais[4],
        totais[5]
    )
    tree.insert("", "end", values=totais_formatados)

    # Inserir rendimento
    rendimento_formatado = (
        "Rendimento",
        "",
        "",
        "",
        f"{round(rendimento * 100, 2)}%" if rendimento is not None else "N/A"
    )
    tree.insert("", "end", values=rendimento_formatado)

    tree.pack(fill="both", expand=True, padx=10, pady=10)
    ttk.Button(novaJanela, text="Fechar", command=novaJanela.destroy).pack(pady=5)

def gerar_grafico(dados):
    plotar_graficos(dados)

def criar_campos_pontos(janela, num_pontos):
    # Define widget scrollbar
    canvas = tk.Canvas(janela)
    scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    frame_scroll = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scroll.bind("<Configure>", on_configure)
    entries = []

    for i in range(num_pontos):
        # Frame para scrollbar
        frame = ttk.Frame(frame_scroll, padding="10")
        frame.grid(row=i, column=0, pady=5)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Labels e campos de texto (para pressão, volume e temperatura)
        label_p = ttk.Label(frame, text=f"Ponto {i+1} - Pressão (Pa):", anchor="center", justify="center")
        label_p.grid(row=0, column=0, sticky="e", padx=5)
        entry_p = ttk.Entry(frame, justify="center", width=20)
        entry_p.grid(row=0, column=1, sticky="w", padx=5)

        label_v = ttk.Label(frame, text=f"Ponto {i+1} - Volume (m³):", anchor="center", justify="center")
        label_v.grid(row=1, column=0, sticky="e", padx=5)
        entry_v = ttk.Entry(frame, justify="center", width=20)
        entry_v.grid(row=1, column=1, sticky="w", padx=5)

        label_t = ttk.Label(frame, text=f"Ponto {i+1} - Temperatura (K):", anchor="center", justify="center")
        label_t.grid(row=2, column=0, sticky="e", padx=5)
        entry_t = ttk.Entry(frame, justify="center", width=20)
        entry_t.grid(row=2, column=1, sticky="w", padx=5)

        # Adiciona os valores inseridos em uma lista
        entries.append((entry_p, entry_v, entry_t))

    # Botões centralizados
    botoes_frame = ttk.Frame(frame_scroll, padding=10)
    botoes_frame.grid(row=num_pontos, column=0, pady=10)

    calcular_button = ttk.Button(botoes_frame, text="Calcular", command=lambda: abrirJanelaResultados(capturar_dados(entries)))
    calcular_button.pack(side="left", padx=10)

    grafico_button = ttk.Button(botoes_frame, text="Gerar Gráfico", command=lambda: gerar_grafico(capturar_dados(entries)))
    grafico_button.pack(side="left", padx=10)

    return entries



def exibir_campos_pontos():
    # Tratamento de exceção
    try:
        # Cria os campos de acordo com a quantidade de pontos determinada
        num_pontos = int(entrada_num_pontos.get())
        if num_pontos < 2:
            raise ValueError("Insira pelo menos 2 pontos.")
        janela_num_pontos.pack_forget()
        janela_campos_pontos.pack(fill="both", expand=True)
        # Chama a função criar_campos_pontos
        criar_campos_pontos(janela_campos_pontos, num_pontos)
        botao_voltar.place(x=10, y=10)  
    except Exception as e:
        tk.messagebox.showinfo("Erro", "Digite um valor numérico, maior ou igual a 2!")

def voltar_tela_inicial():
    # Destrói os widget: labels, campos de texto e botões
    for widget in janela_campos_pontos.winfo_children():
        widget.destroy()
    janela_campos_pontos.pack_forget()
    # Retorna à tela inicial
    janela_num_pontos.pack(fill="both", expand=True)



# Janela principal
janelaPrincipal = tk.Tk()
janelaPrincipal.title("Calculadora Termodinâmica")
janelaPrincipal.geometry("500x400")
janelaPrincipal.configure(bg="#f0f0f0")

# Imagem
imagem = Image.open("images/Logo_CTUP__1_-removebg-preview.png")
imagem = imagem.resize((280, 140))  # largura x altura em pixels
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janelaPrincipal, image=imagem_tk, bg="#f0f0f0")
label_imagem.pack(pady=10)

# Botão de voltar no canto superior esquerdo
botao_voltar = ttk.Button(janelaPrincipal, text="Voltar", command=voltar_tela_inicial)
botao_voltar.pack_forget()

# Tela 1: Solicitar número de pontos
janela_num_pontos = tk.Frame(janelaPrincipal)
janela_num_pontos.pack(fill="both", expand=True)
label_num_pontos = ttk.Label(janela_num_pontos, text="Digite o número de pontos:")
label_num_pontos.pack(pady=10)
entrada_num_pontos = ttk.Entry(janela_num_pontos, justify="center")
entrada_num_pontos.pack(pady=10)
botao_num_pontos = ttk.Button(
    janela_num_pontos,
    text="Confirmar",
    command=exibir_campos_pontos
)
botao_num_pontos.pack(pady=10)

# Tela 2: Campos dinâmicos para pontos
janela_campos_pontos = tk.Frame(janelaPrincipal)

# Iniciar a interface
janelaPrincipal.mainloop()
