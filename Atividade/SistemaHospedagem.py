import customtkinter as ctk

ctk.set_appearance_mode("dark")


#FUNÇÕES:
def calcularReseva():
    try:
        nome = nomeHospede.get()
        quantidade = int(quantidadeDiarias.get())
        valor = float(valorDiaria.get())
        
        #VALIDANDO OS VALORES
        if quantidade < 0 :
            resultado1.configure(text=f"Quantidade inválida de diárias.")
        elif valor < 0:
            resultado1.configure(text=f"Quantidade inválida de valor para diária.")
        
        #APLICANDO OS CALCULOS
        elif quantidade >=5:
            desconto = quantidade*valor*0.10
            resultado1.configure(text=f"Nome do Hóspede: {nome}\nHospedagem: R${quantidade*valor:.2f}\nDesconto: R${desconto:.2f}\n________________\n\nTotal a pagar: R${quantidade*valor - desconto:.2f} ",text_color = "white")
        else:
            desconto = 0
            resultado1.configure(text=f"Nome do Hóspede: {nome}\nHospedagem: R${quantidade*valor:.2f}\nDesconto: R${desconto:.2f}\n________________\n\nTotal a pagar: R${quantidade*valor - desconto:.2f} ", text_color = "white")
    except:
        resultado1.configure(text=f"Um ou mais valores inválidos. Operação abortada.", text_color = "red")

#JANELA PRINCIPAL
janela = ctk.CTk()
janela.geometry("750x550")
janela.resizable(False,False)
janela.title("Reserva de Hotel")

#JANELAS DE INPUT COM TITULO
tituloHospede = ctk.CTkLabel(janela,
                             text="Nome do Hóspede:",
                             text_color="white",
                             font=("Arial",12,"bold"))
tituloHospede.pack(pady = 20)
nomeHospede = ctk.CTkEntry(janela,
                           width=400,
                           height=40,
                           border_color="light blue",
                           placeholder_text="Digite o nome do Hóspede.")
nomeHospede.pack()


tituloDiarias = ctk.CTkLabel(janela,
                             text="Quantidade de Diárias:",
                             text_color="white",
                             font=("Arial",12,"bold"))
tituloDiarias.pack(pady = 20)
quantidadeDiarias = ctk.CTkEntry(janela,
                           width=400,
                           height=40,
                           border_color="light blue",
                           placeholder_text="Digite a quantidade de diárias.")
quantidadeDiarias.pack()


tituloValor = ctk.CTkLabel(janela,
                             text="Valor da Diária(R$):",
                             text_color="white",
                             font=("Arial",12,"bold"))
tituloValor.pack(pady = 20)
valorDiaria = ctk.CTkEntry(janela,
                           width=400,
                           height=40,
                           border_color="light blue",
                           placeholder_text="Digite o valor da diária.")
valorDiaria.pack()

#BOTÃO
botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text="CALCULAR HOSPEDAGEM",
                      fg_color="blue",
                      border_color="blue",
                      text_color="white",
                      cursor="hand2",
                      font=("Arial",15,"bold"),
                      command= calcularReseva)
botao.pack(pady = 20)

# RESULTADOS DOS CALCULOS
resultado1 = ctk.CTkLabel(janela,
                         text="",
                         text_color="white",
                         font=("Times new Roman",15,"bold"))
resultado1.pack(pady = 5)




janela.mainloop()