import contatos

menu = [
    "Novo contato", 
    "Lista de contatos",
    "Editar contato",
    "Favoritar/Desfavoritar contato",
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

def input_fields(titulo, old_nome="", old_telefone="", old_email=""):
    print(titulo)
    nome = input(f"Nome [{old_nome}]:")
    telefone = input(f"Telefone [{old_telefone}]:")
    email = input(f"E-mail [{old_email}]:")
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
            nome, telefone, email = input_fields("Digite as informações do novo contato")
            sucesso = contatos.adicionar_usuario(nome, telefone, email)
            if sucesso:
                print("\nContato incluído com sucesso.")
            else:
                print("\nFalha na inclusão do contato. O nome é obrigatório. Verifique as informações digitadas.")
        elif escolha == 2:
            contatos.listar_contatos()
        elif escolha == 3:
            contato_id = selecionar_contato("Digite o número do contato")
            old_nome, old_telefone, old_email = contatos.obter_contato_por_id(contato_id)
            nome, telefone, email = input_fields("Digite as novas informações do novo contato", old_nome, old_telefone, old_email)
            mensagem = contatos.editar_contato(contato_id, nome, telefone, email)
            print(mensagem)
        elif escolha == 4:
            contato_id = selecionar_contato("Digite o número do contato")
            mensagem = contatos.favoritar(contato_id)
            print(mensagem)
        elif escolha == 5:
            contatos.listar_contatos(favoritos=True)
        elif escolha == 6:
            print("\nPrograma finalizado!")
            quit()