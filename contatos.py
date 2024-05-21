contatos = []

def adicionar_usuario(nome, telefone, email=""):
    if nome == "":
        return False
    
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(novo_contato)
    return True

def listar_contatos(favoritos=False):
    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.")
        return

    print("\nLista de contatos:\n")
    for index, contato in enumerate(contatos):
        if (favoritos and contato["favorito"]) or favoritos == False:
            favorito = " ★ " if contato["favorito"] else "   "
            print(f"{index + 1}. [{favorito}] {contato['nome']} - {contato['telefone']} - {contato['email']}")
    return

def editar_contato(index, nome, telefone, email):
    if nome == "":
        return "\nFalha na atualização do contato. O nome é obrigatório."

    contatos[index]["nome"] = nome
    contatos[index]["telefone"] = telefone
    contatos[index]["email"] = email
    return "\nContato atualizado com sucesso!"

def favoritar(index):
    if contatos[index]["favorito"]:
        prefixo = "des"
        favorito = False
    else:
        prefixo = ""
        favorito = True
    contatos[index]["favorito"] = favorito
    return f"\nContato {prefixo}favoritado com sucesso!"

def obter_contato_por_id(index):
    nome = contatos[index]["nome"]
    telefone = contatos[index]["telefone"]
    email = contatos[index]["email"]
    return nome, telefone, email