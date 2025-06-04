import tkinter as tk

# Função para capturar o valor digitado
def capturar_valor():
    valor = entrada.get()  # Obtém o texto digitado na Entry
    label_resultado.config(text=f"Você digitou: {valor}")
    return valor

# Configuração da janela principal
janela = tk.Tk()
janela.title("Exemplo de Entry no Tkinter")

# Label de instrução
label_instrucao = tk.Label(janela, text="Digite a temperatura:")
label_instrucao.pack(pady=5)

# Caixa de texto (Entry)
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=5)

# Botão para capturar o valor
botao = tk.Button(janela, text="Enviar", command=capturar_valor)
botao.pack(pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5)

# Inicia o loop da interface
janela.mainloop()

temperatura = capturar_valor()
