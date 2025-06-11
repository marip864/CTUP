import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def capturar_dados():
    pressao = entrada_pressao.get()
    temperatura = entrada_temperatura.get()
    try:
        pressao = float(pressao)
        temperatura = float(temperatura)
        abrirJanela(pressao, temperatura)
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

def abrirJanela(p, t):
    novaJanela = tk.Toplevel()
    novaJanela.title("Gráficos")

    tk.Label(novaJanela, text=f"Dados recebidos: {p} atm e {t} K").pack(pady=10)

    # Criar gráfico
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3], [p, t, p + t], marker='o')
    ax.set_title("Gráfico de Exemplo")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")

    canvas = FigureCanvasTkAgg(fig, master=novaJanela)
    canvas.draw()
    canvas.get_tk_widget().pack()

    tk.Button(novaJanela, text="Fechar", command=novaJanela.destroy).pack(pady=10)

# Janela principal
janela = tk.Tk()
janela.title("Entrada de Dados")

tk.Label(janela, text="Pressão (atm):").pack()
entrada_pressao = tk.Entry(janela)
entrada_pressao.pack()

tk.Label(janela, text="Temperatura (K):").pack()
entrada_temperatura = tk.Entry(janela)
entrada_temperatura.pack()

tk.Button(janela, text="Gerar Gráfico", command=capturar_dados).pack(pady=10)

janela.mainloop()
