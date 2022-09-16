from os import remove
agenda = []
escolha = ""

while escolha != '0':
    print('=========================')
    print('==== Programa Agenda ====')
    print('=========================')
    print('= 1 - Cadastrar contato =')
    print('= 2 - Pesquisar contato =')
    print('= 3 - Atualizar contato =')
    print('= 4 - Apagar contato    =')
    print('= 5 - Listar todos      =')
    print('= 0 - Sair              =')
    print('=========================')
    escolha = input('Escolha sua opção: ')

    if escolha == '1':  # Adicionando contatos
        print()
        print('Módulo de cadastro:\n')

        contato = []
        contato.clear()
        nome = input('Insira o nome: ')
        contato.append(nome)
        nume = input('Insira o contato: ')
        contato.append(nume)
        email = input('Insira o email: ')
        contato.append(email)
        agenda.append(contato)  # Passando pra lista

    elif escolha == '2':  # Função de pesquisa
        print()
        print('Módulo de pesquisa: \n')
        nome_bus = input('Insira o nome que você quer procurar: ')
        achou = False
        for pessoa in agenda:
            # busca pelo nome nesta lista
            if nome_bus.upper() in pessoa[0].upper() and not achou:
                print()
                print('Nome:\t', pessoa[0])
                print('Número:\t', pessoa[1])
                print('Email:\t', pessoa[2])
                print()
                achou = True
        print()
        if not achou:
            print('Nome não encontrado')
        print()

    elif escolha == '3':  # Função para atualizar o contato
        print()
        print('Módulo de Atualização:\n')
        nome_bus = input('Nome a procurar: ')
        achou = False
        for pessoa in agenda:
            # Mesma estrutura do módulo de busca
            if nome_bus in pessoa and not achou:
                print(pessoa)
                print()
                print('Contato atual:\n')
                print('Nome:\t', pessoa[0])
                print('Número:\t', pessoa[1])
                print('Email:\t', pessoa[2])
                agenda.remove(pessoa)

                att = []
                att.clear()
                print('\nAgora você aplicará as mudanças no contato \n')
                nome2 = input('Insira a mudança no nome: ')
                att.append(nome2)
                nume = input('Insira a mudança no número: ')
                att.append(nume)
                email = input('Insira a mudança no email: ')
                att.append(email)
                agenda.append(att)
                achou = True
        if not achou:
            print('Nome não encontrado')
        else:
            print('As mudanças foram aplicadas')
        print()

    elif escolha == '4':  # Função para excluir
        print()
        print('Módulo de Exclusão:\n')
        nome_bus = input('Nome a procurar: ')
        achou = False
        for pessoa in agenda:
            if nome_bus in pessoa and not achou:
                ex = input('Quer excluir este contato(S/N)?\t')
                if ex.upper() == "S":
                    agenda.remove(pessoa)
                else:
                    print('O contato não foi excuido')
                    break
                achou = True
        if nome_bus not in agenda:
            print('Nome não encontrado')
        print()

    elif escolha == '5':
        print()
        print('Módulo de listagem:\n')
        cont = 1
        for i in agenda:  # lista todos os contatos presentes na lista
            print('Contato %d:' % (cont))
            print('Nome:\t', i[0])
            print('Número:\t', i[1])
            print('Email:\t', i[2])
            print()
            cont += 1
        print()

    elif escolha == '0':
        print()
        print('Módulo de encerramento!\n')
    else:
        print('Módulo invalido!')

print('Até a proxima!')
