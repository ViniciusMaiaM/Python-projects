print('Informe a data')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
mes31 = [1, 3, 5, 7, 8, 10, 12]
mes30 = [3, 6, 9, 11]
if ano == 0:
    print('Ano não valido')

elif mes < 1 or mes > 12:
    print('Mês não valido')

elif ((ano % 4) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0):
    if mes == 2 and dia > 29:
        print('Dia Invalido para o mês de Fevereiro')

    else:
        print(ano, 'é bissexto!')
        print('A data é %d/%d/%d' % (dia, mes, ano))
        exit()

if mes in mes31 and dia > 31:
    if mes == 1:
        print('Dia Invalido para Janeiro')
    elif mes == 3:
        print('Dia Invalido para Março')
    elif mes == 5:
        print('Dia Invalido para Maio')
    elif mes == 7:
        print('Dia Invalido para Julho')
    elif mes == 8:
        print('Dia Invalido para Agosto')
    elif mes == 10:
        print('Dia Invalido para Outubro')
    elif mes == 12:
        print('Dia Invalido para Dezembro')

elif mes in mes31 and dia > 30:
    if mes == 3:
        print('Dia Invalido para Março')
    if mes == 6:
        print('Dia Invalido para Junho')
    if mes == 9:
        print('Dia Invalido para Setembro')
    if mes == 11:
        print('Dia Invalido para Novembro')

elif mes == 2 and dia > 28:
    print('Dia Invalido para Fevereiro')

else:
    print('A data é %d/%d/%d' % (dia, mes, ano))
    print('Fim do programa!')
