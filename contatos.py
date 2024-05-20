contatos = []

def adicionar_usuario(nome, telefone, email=""):
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(novo_contato)
    return True

def listar_contatos():
    for index, contato in enumerate(contatos):
        favorito = " ★ " if contato["favorito"] else "   "
        print(f"{index + 1}. [{favorito}] {contato['nome']} - {contato['telefone']} - {contato['email']}")
    return

def editar_contato(index, nome, telefone, email):
    contatos[index]["nome"] = nome
    contatos[index]["telefone"] = telefone
    contatos[index]["email"] = email
    return

def favoritar(index):
    if contatos[index]["favorito"]:
        prefixo = "des"
        favorito = False
    else:
        prefixo = ""
        favorito = True
    contatos[index]["favorito"] = favorito
    print(f"Contato {prefixo}favoritado com sucesso")
    return