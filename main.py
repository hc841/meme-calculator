import tkinter as tk

def concatenar_numeros():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    resultado = num1 + num2
    label_resultado.config(text="Resultado da concatenação: " + resultado)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Widgets
label_num1 = tk.Label(janela, text="Digite o primeiro número:")
entry_num1 = tk.Entry(janela)

label_num2 = tk.Label(janela, text="Digite o segundo número:")
entry_num2 = tk.Entry(janela)

btn_concatenar = tk.Button(janela, text="Somar", command=concatenar_numeros)

label_resultado = tk.Label(janela, text="Resultado da Soma:")

# Posicionar os widgets na janela
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

btn_concatenar.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado.grid(row=3, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
janela.mainloop()
