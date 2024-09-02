
# Na parte de menu sempre lembrar de usar """ no inicio de no fim, assim podendo fazer uma string de forma mais livre sem ter que usar print para cada linha

menu = """
======MENU======

SELECIONE UMA OPÇÃO:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair



=> """

# Na parte das variaveis,e dado os valores que quermos nelas de acordo com o oque e pedido no exercicio(RESALVA PARA EXTRATO QUE ESTA COMO VALOR STRING "")

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


# Começamos, usnado WHILE TRUE, por que queremos que nosso programa fique em loop ate o usuario decidir sair dele

while True:

# aki criamos a variavel OPÇAO e damos o valor dela ao menu criado anteriormente, para que o sistema reconheça as opçoes digitadas pelo usuario
# e venha apresentar os valores desejados de acordo com oque ele pede
    opcao = input(menu)
    
    if opcao == "1":    # inicio da sequencia de decisao                                          
        valor = float(input('Digite o valor de Deposito:'))# pergunto ao meu usuario O valor que ele deseja

        if valor > 0: #Primeira verificação feita, que no caso e perguntando se o 'valor' e maior que 0, assim evitando depositos de numero negativos. exp: -100
            saldo += valor #O 'valor' sendo maior que 0 usamos '+=' para adicionar o valor informado a variavel 'saldo'
            extrato += f"Depóstio : R$ {valor: .2f}\n"#Logo apos adicionarmos o valor a variavel saldo,concatenamos o extrado e saldo, para adicionar o 'saldo' a 'extrato'
        
        else:
            print('Operação falhou! O valor informado e invalido') #caso nenhuma das opçoes acima seja atendida, ira retornar o print
    
    elif opcao == '2':
        valor = float(input('Informe o valor de saque:'))# pergunto ao meu usuario O valor que ele deseja

        excedeu_saldo = valor > saldo#Primeira verificação, se o saque excedeu o valor de saldo em conta

        excedeu_limite = valor > limite#Segunda verificação, Se o saque excedeu o valor permitido pra saque, que e de 500 reais(criterio do exercicio)
 
        excedeu_saques = numero_saque >= LIMITE_SAQUE#Terceira verificação,Se excedeu a quantiodade de saque permitido, que e de 3(criterio do exercicio)

        if excedeu_saldo:
            print('Operção falhou! Você não tem saldo suficiente.')#Caso a verificação de saque exceda o valor em conta
        
        elif excedeu_limite:
            print('Opeção falhou! Você excedeu o valor de saque permitido.')#Caso a segunda verificação, tenha excedido o valor de saque de 500 reais

        elif excedeu_saques:
            print('Operaçãp falhou! Você excedeu o limite de saques permitidos.')#Caso a terceira verificação, tenha excedido a quantidade de saque permitida, que e de 3

        elif valor > 0:#Aki colocamos o elif, para uma outra verificaçao, que o valor sacado tem que ser > 0, pois nao tem como sacar um valor negativo
            saldo -= valor#Subtraimos o valor sacado do saldo da conta
            extrato += f"saque: R$ {valor:.2f}\n"#E concatenamos o valor do saldo, para o extrado, assim mostrando o valor correto em extrado
            numero_saque += 1#Numero de saques ja feito

        else:
            print('Operação falhou! O valor informado e invalido')#Quando nenhuma verificaçao e correta


    elif opcao == '3':
        print("\n================ EXTRATO ================")#cabeçalho
        print("Não foram realizadas movimentações." if not extrato else extrato)#mostrando que caso nao tenha feito movimentaçoes, o exztrato começa vazio
        print(f"\nSaldo: R$ {saldo:.2f}")#mostrando o valor de saldo, seguindo regra de negocios
        print("==========================================")#roda pe


    elif opcao == '4':#finalizar o loop de repetição
        break

    else:#caso o usuario coloque qualquer valor nas opçoes,caso nao seja as pedida
        print('Operação invalida, por favor selecione uma das opções informadas')