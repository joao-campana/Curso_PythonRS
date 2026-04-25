def adicionar_contato(contatos, nome, telefone, email, favorito=False):
    contato = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": favorito}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        fav = "★" if contato["Favorito"] else ""
        print(f"{indice}. {contato['Nome']} - {contato['Telefone']} - {contato['Email']} {fav}")

def editar_contato(contatos, indice):
    if indice < 0 or indice >= len(contatos):
        print("Índice inválido.")
        return
    contato = contatos[indice]
    print(f"Editando contato: {contato['Nome']}")
    print("Campos: 1. Nome, 2. Telefone, 3. Email")
    campo = input("Escolha o campo a editar (1-3): ")
    if campo == '1':
        novo = input("Novo nome: ")
        contato["Nome"] = novo
    elif campo == '2':
        novo = input("Novo telefone: ")
        contato["Telefone"] = novo
    elif campo == '3':
        novo = input("Novo email: ")
        contato["Email"] = novo
    else:
        print("Campo inválido.")
    print("Contato atualizado.")

def marcar_favorito(contatos, indice):
    if indice < 0 or indice >= len(contatos):
        print("Índice inválido.")
        return
    contatos[indice]["Favorito"] = True
    print(f"{contatos[indice]['Nome']} marcado como favorito.")

def desmarcar_favorito(contatos, indice):
    if indice < 0 or indice >= len(contatos):
        print("Índice inválido.")
        return
    contatos[indice]["Favorito"] = False
    print(f"{contatos[indice]['Nome']} desmarcado como favorito.")

def listar_favoritos(contatos):
    favoritos = [c for c in contatos if c["Favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
        return
    print("\nContatos Favoritos:")
    for indice, contato in enumerate(favoritos, start=1):
        print(f"{indice}. {contato['Nome']} - {contato['Telefone']} - {contato['Email']}")

def apagar_contato(contatos, indice):
    if indice < 0 or indice >= len(contatos):
        print("Índice inválido.")
        return
    nome = contatos[indice]["Nome"]
    contatos.pop(indice)
    print(f"Contato {nome} apagado.")

contatos = []

while True:
    print("\nMenu da Lista Telefônica:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Marcar como favorito")
    print("5. Desmarcar como favorito")
    print("6. Visualizar favoritos")
    print("7. Apagar contato")
    print("8. Sair")

    escolha = input("Escolha uma opção (1-8): ")
    if escolha == '1':
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        while True:
            fav_input = input("Favorito? (s/n): ").lower()
            if fav_input in ['s', 'n']:
                fav = fav_input == 's'
                break
            else:
                print("Entrada invalida, digite s ou n!")
        adicionar_contato(contatos, nome, telefone, email, fav)

    elif escolha == '2':
        listar_contatos(contatos)

    elif escolha == '3':
        listar_contatos(contatos)
        while True:
            indice_str = input("Número do contato a editar (0 para voltar ao menu principal): ")
            if indice_str == '0':
                break
            try:
                indice = int(indice_str) - 1
                if 0 <= indice < len(contatos):
                    editar_contato(contatos, indice)
                    break
                else:
                    print("Numero Invalido, Coloque um Numero Valido!")
            except ValueError:
                print("Numero Invalido, Coloque um Numero Valido!")

    elif escolha == '4':
        listar_contatos(contatos)
        while True:
            indice_str = input("Número do contato a marcar como favorito (0 para voltar ao menu principal): ")
            if indice_str == '0':
                break
            try:
                indice = int(indice_str) - 1
                if 0 <= indice < len(contatos):
                    marcar_favorito(contatos, indice)
                    break
                else:
                    print("Numero Invalido, Coloque um Numero Valido!")
            except ValueError:
                print("Numero Invalido, Coloque um Numero Valido!")

    elif escolha == '5':
        listar_contatos(contatos)
        while True:
            indice_str = input("Número do contato a desmarcar como favorito (0 para voltar ao menu principal): ")
            if indice_str == '0':
                break
            try:
                indice = int(indice_str) - 1
                if 0 <= indice < len(contatos):
                    desmarcar_favorito(contatos, indice)
                    break
                else:
                    print("Numero Invalido, Coloque um Numero Valido!")
            except ValueError:
                print("Numero Invalido, Coloque um Numero Valido!")

    elif escolha == '6':
        listar_favoritos(contatos)

    elif escolha == '7':
        listar_contatos(contatos)
        while True:
            indice_str = input("Número do contato a apagar (0 para voltar ao menu principal): ")
            if indice_str == '0':
                break
            try:
                indice = int(indice_str) - 1
                if 0 <= indice < len(contatos):
                    apagar_contato(contatos, indice)
                    break
                else:
                    print("Numero Invalido, Coloque um Numero Valido!")
            except ValueError:
                print("Numero Invalido, Coloque um Numero Valido!")

    elif escolha == '8':
        print("Saindo...")
        break
    else:
        print("Numero Invalido, Coloque um Numero Valido!")