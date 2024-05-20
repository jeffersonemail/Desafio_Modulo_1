import contatos

menu = [
    "Novo contato", 
    "Lista de contatos",
    "Editar contato",
    "Favoritar contato",
    "Listar favoritos",
    "Apagar contato"
]

def selecionar_contato(mensagem):
    contatos.listar_contatos()
    try:
        contato_id = int(input(f"{mensagem}:"))
    except Exception as e:
        print(f"Opção inválida. {e}")
        contato_id = 0
    finally:
        return contato_id - 1

def montar_menu():
    for index, opcao in enumerate(menu):
        print(index + 1, "-", opcao)

    return input("Escolha uma opção: ")

def input_fileds(titulo):
    print(titulo)
    nome = input("Nome:")
    telefone = input("Telefone:")
    email = input("E-mail:")
    return nome, telefone, email


while True:
    print("\nAgenda de contatos\n")
    escolha = montar_menu()
    
    try:
        escolha = int(escolha)
        if escolha < 1 or escolha > len(menu):
            raise ValueError(f"Escolha um número de 1 a {len(menu)}.")
    except Exception as e: 
        print(e)
    else: 
        if escolha == 1:
            input_fileds("Digite as informações do novo contato")
            sucesso = contatos.adicionar_usuario(nome, telefone, email)
            if sucesso:
                print("Contato incluído com sucesso.")
            else:
                print("Falha na inclusão do contato.")
        elif escolha == 2:
            contatos.listar_contatos()
        elif escolha == 3:
            contato_id = selecionar_contato("Digite o número do contato")
            mensagem = contatos.editar_contato(contato_id)
        elif escolha == 4:
            contato_id = selecionar_contato("Digite o número do contato")
            mensagem = contatos.favoritar(contato_id)
            print(mensagem)
        elif escolha == 6:
            quit()
