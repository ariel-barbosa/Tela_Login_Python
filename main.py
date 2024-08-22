import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# Criação da janela
janela = customtkinter.CTk()
janela.geometry('300x350')

# função do clique do botão
def clique():
    print("Opa")


# Texto principal
texto = customtkinter.CTkLabel(janela, text='Bem-Vindo(a)', font=('Arial',19))
texto.pack(padx=30, pady=30)


# Entradas de email e senha
email = customtkinter.CTkEntry(janela, placeholder_text='email...')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='senha...', show="*")
senha.pack(padx=10, pady=10)

# Lembrar Senha
checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar senha', font=('Arial',12))
checkbox.pack(padx=5, pady=5)


btn = customtkinter.CTkButton(janela, text='Login', command=clique)
btn.pack(padx=40, pady=40)



janela.mainloop()