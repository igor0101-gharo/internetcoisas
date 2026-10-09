import customtkinter as ctk
ctk.set_appearance_mode('dark')

#===============================
janela = ctk.CTk()
janela.geometry('600x450')
janela.resizable(False,False)
janela.title('Resultado Acadêmico')
#==================================


#============= Nome do Aluno ====================
titulo = ctk.CTkLabel(janela,
                    text='Nome do Aluno:',
                    font=('Verdana',15,'bold'),
                    )
titulo.pack(pady=5)
nome = ctk.CTkEntry(janela,
                    width=550,
                    height=40,
                    placeholder_text="Digite o nome do Aluno")
nome.pack()
#==============================================================



#=============== Nota 1 =================
nota1Titulo = ctk.CTkLabel(janela,
                    text='1º nota:',
                    font=('Verdana',15,'bold'),
                    )
nota1Titulo.pack(pady=5)
nota1 = ctk.CTkEntry(janela,
                    width=550,
                    height=40,
                    placeholder_text="Digite a 1º nota")
nota1.pack()
#================================================



#================ Nota 2 ==================
nota2Titulo = ctk.CTkLabel(janela,
                    text='2º nota:',
                    font=('Verdana',15,'bold'),
                    )
nota2Titulo.pack(pady=5)
nota2 = ctk.CTkEntry(janela,
                    width=550,
                    height=40,
                    placeholder_text="Digite a 2º nota")
nota2.pack()
#==========================================



#================== Função =====================
def calcularMedia():
    try:
        n1 = float(nota1.get())
        n2 = float(nota2.get())

        media = (n1+n2) / 2

        if (n1 > 10 or n2 > 10):
            resultado.configure(text='As notas estão inválidas, tente novamente!!', text_color='red')
        elif (n1 < 0 or n2 < 0):
            resultado.configure(text='As notas estão inválidas, tente novamente!!', text_color='red')
        else:
            if media < 5:
                resultado.configure(text=f'Aluno: {nome.get()}  \nSituação: Reprovado!! \nMédia: {media:.1f}',text_color = 'red')
            elif media >= 5 and media <=6.9:
                resultado.configure(text=f'Aluno: {nome.get()}  \nSituação: Recuperação!! \nMédia: {media:.1f}', text_color = 'yellow')
            else:
                resultado.configure(text=f'Aluno: {nome.get()}  \nSituação: Aprovado!! \nMédia: {media:.1f}', text_color='green')

    except:
        resultado.configure(text='Digite um valor válido!!')
#=====================================================





#=============== Botão ===================
btn = ctk.CTkButton(janela,
                    width=550,
                    height=35,
                    text='Calcular Resultado',
                    font=('verdana',15,'bold'),
                    cursor='hand2',
                    border_width=1,
                    border_color='white',
                    command=calcularMedia)
btn.pack(pady=40)
#==================================



resultado = ctk.CTkLabel(janela,
                        text='',
                        font=('verdana',18,'bold'))
resultado.pack(pady=5)

janela.mainloop()