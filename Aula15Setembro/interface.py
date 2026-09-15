import customtkinter as ctk

ctk.set_appearance_mode('dark')


#Janela -------------
janela = ctk.CTk()
janela.geometry("500x300")
janela.resizable(False,False)
janela.title('Sistema de Acesso - 2026')
janela.iconbitmap("Aula15Setembro/Login_37128.ico")
#-------------------------


#corpo da janela---------
titulo = ctk.CTkLabel(janela, 
                      text = 'Sistema de Login',
                      text_color="#36792a",
                      font = ('arial',50))
titulo.pack()



login = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color='#36792a',
                     placeholder_text='Digite o login')
login.pack(pady = 30)



senha = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color='#36792a',
                     placeholder_text='Digite a senha',
                     show='•')
senha.pack()


botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text='Acessar',
                      fg_color='#36792a',
                      text_color='white',
                      cursor='hand2',
                      font=('arial',30))
botao.pack(pady=30)









janela.mainloop()