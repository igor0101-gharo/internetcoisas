import customtkinter as ctk

ctk.set_appearance_mode('dark')


def calcularMedia():
    try:
        n1 = float(nota1.get())
        n2 = float(nota2.get())
        n3 = float(nota3.get())
    
    
        formula= (n1+n2+n3)/3
        if formula > 5:
            resultado.configure(text =f"Média: {formula:.2f}\nAPROVADO", text_color = "green")
        else:
            resultado.configure(text =f"Média: {formula:.2f}\nREPROVADO", text_color = "red")
    except:
        resultado.configure(text="Umas ou mais notas inválidas. Digite apenas números", text_color = "white")
    


janela = ctk.CTk()
janela.geometry("600x450")
janela.resizable(False,False)
janela.title("Sistema Escola")


titulo = ctk.CTkLabel(janela,
                      text="Sistema Escola",
                      text_color="yellow",
                      font=('Arial',45,"bold"))
titulo.pack()

nota1 = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color="yellow",
                     placeholder_text="Digite a sua nota na 1ª unidade")
nota1.pack(pady = 20)


nota2 = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color="yellow",
                     placeholder_text="Digite a sua nota na 2ª unidade")
nota2.pack(pady = 20)


nota3 = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color="yellow",
                     placeholder_text="Digite a sua nota na 3ª unidade")
nota3.pack(pady = 20)


botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text = "Resultado",
                      fg_color="yellow",
                      border_width=2,
                      border_color="yellow",
                      text_color="black",
                      cursor = 'hand2',
                      font=('Times new Roman',15,"bold"),
                      command= calcularMedia)
botao.pack(pady = 20)

resultado =ctk.CTkLabel(janela,
                       text='',
                       text_color="white",
                       font=("Times new Roman",15))
resultado.pack(pady = 10)




































janela.mainloop()