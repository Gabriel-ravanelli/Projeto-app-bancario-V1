from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:#Criação da classe 'cliente'
    def __init__(self, endereco):#estrutura criada da classe cliente, conta nao esta incluso, pois sera atribuido nas estruturas abaixo
        self.endereco = endereco#atribuindo valores aos atributos da classe
        self.contas = []#atributo atribuido, como lista, pois ira armazenar mais de uma conta

    def realizar_transacao(self, conta, transacao):#estrutura de um atributo criado, para ser usado como realizar transaçaão entre as contas
        transacao.registrar(conta)#aki ele tras o registrar de 'transação'

    def adicionar_conta(self, conta):#adicionando conta e sua estrutura
        self.contas.append(conta)# aki ele tras a opçao de conta que sera criado a classe loga abaixo desse atributo


class PessoaFisica(Cliente):#criação da classe pessoa fisica(que usa herança da classe cliente)
    def __init__(self, nome, data_nascimento, cpf, endereco):#aki temos o metodo da estrutura e seus atributos da classe pessoa fisica
        super().__init__(endereco)#aki temos a utilização da função super, para pegar a estrutra de endereço da classe 'cliente'
        self.nome = nome#dando valor ao atributo nome
        self.data_nascimento = data_nascimento#dando valor ao atributo data nascimento
        self.cpf = cpf#dando valor ao atributo cpf


class Conta:#criação da classe conta criado
    def __init__(self, numero, cliente):#metodo da estrutura dos atributos da conta
        self._saldo = 0#dando valor ao atributo
        self._numero = numero##dando valor ao atributo
        self._agencia = "0001"##dando valor ao atributo
        self._cliente = cliente##dando valor ao atributo
        self._historico = Historico()#

    @classmethod#mapeado o classmethod da classe de nova conta que recebe os atributos de cliente e numero
    def nova_conta(cls, cliente, numero):#criação da estrutura nova conta
        return cls(numero, cliente)#retorna uma instancia de conta

    @property# propriedades para acessar os valor de saldo( que e um valor privado)
    def saldo(self):#
        return self._saldo#

    @property## propriedades para acessar os valor de numero( que e um valor privado)
    def numero(self):#
        return self._numero#

    @property## propriedades para acessar os valor de agencia( que e um valor privado)
    def agencia(self):#
        return self._agencia#

    @property## propriedades para acessar os valor de cliente( que e um valor privado)
    def cliente(self):#
        return self._cliente#

    @property## propriedades para acessar os valor de historico( que e um valor privado)
    def historico(self):#
        return self._historico#

    def sacar(self, valor):#Criado o metodo da operação sacar e seus atributos
        saldo = self.saldo#aki damos valor ao atributo saldo.(ele ja recebeu o valor de 0, na estrutura acima, mas damos outro valor para ele aki)
        excedeu_saldo = valor > saldo#Aki damos o valor de excedeu saldo, pois para o saque ser efetuado, o valor sacado nao pode ser maior que o saldo em conta

        if excedeu_saldo:#aki temos uma condição
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")#retorno da condição

        elif valor > 0:# condição criada, que caso o valor informado for maior que 0, o saque vai ser realizado
            self._saldo -= valor# aki estamos subtraindo o valor de saldo , ao valor sacado
            print("\n=== Saque realizado com sucesso! ===")#retorno da condição
            return True# retorna true, para indentificar que a opeção de saque foi efetuado

        else:#condição caso nenhuma das acima seja atendida
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")#retorno da condição

        return False#retorna falso caso as condiçoes nao seja atendida

    def depositar(self, valor):#metodo depositar criado, e sua estrutura
        if valor > 0:#primeira condição, caso o valor depositado seja maior que 0 o deposito sera efetudao
            self._saldo += valor#aki estaremos adicionando o valor digitado ao saldo da conta do cliente(lembrando que o _saldo um atributo privado, nao podendo ser modificado pelo usuario)
            print("\n=== Depósito realizado com sucesso! ===")#retorno de deposito realizado
        else:#retorno caso a condição acima nao for realizada
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")#
            return False#retorna falso caso nao seja efetuada a condição nao seja atendida

        return True#retorna verdadeiro caso a codição seja atendida


class ContaCorrente(Conta):#classe conta corrente criada( essa classe vai usar de henrança a classe 'cliente')
    def __init__(self, numero, cliente, limite=500, limite_saques=3):#metodo da classe conta corrente e sua estrutura
        super().__init__(numero, cliente)#aki pegamos a informação cliente da classe'cliente', para conseguirmos utilizar ela na classe conta corrente.(para trazer uma henraça e necessario utilizar o 'super()')
        self.limite = limite#dando valor ao atributo limite
        self.limite_saques = limite_saques#dando valor ao atributo limite de saque

    def sacar(self, valor):#aki criamos o metodo saacar e sua estrutura
        numero_saques = len(#aki temos o numero de saque, que colocamos em lista
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]#aki temos uma compreesao de lista, para verificarmos se o tipo da transção efetuada e saque 
        )#

        excedeu_limite = valor > self.limite#aki temos os atributos e os valores que atribuimos a eles, que estao relacionado ao limite de valor de saque
        excedeu_saques = numero_saques >= self.limite_saques#aki temos o outro atributo e o valore que e dado a ele, quando o cliente passa do limite de saque permitido

        if excedeu_limite:#primeira condição criada, quando o valor excede o limite permitido
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")#

        elif excedeu_saques:#segunda condição quando o numero de saque foi excedido
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")#

        else:#retorno, quando o saque deu certo
            return super().sacar(valor)#aki retornamos o 'valor' que vem da calsse conta

        return False#

    def __str__(self):#aki temos a representação da classe e temos a agencia e afins
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:#classe criada historioco
    def __init__(self):#aki temos a criaçao do metodo
        self._transacoes = []#aki temos um lista de transações que estamos mapeando

    @property#propriedade para pegar as transações feitas
    def transacoes(self):#
        return self._transacoes#

    def adicionar_transacao(self, transacao):#aki temos o metodo adicionar transaçao e seus atributos
        self._transacoes.append(#aki e feita a armazenação das transaçoes e uma lista de dicionario
            {
                "tipo": transacao.__class__.__name__,#
                "valor": transacao.valor,#
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),#
            }
        )


class Transacao(ABC):#aki temos a interface de transação que e uma classe absatrata
    @property#o valor que damos para transação
    @abstractproperty#
    def valor(self):#
        pass#

    @abstractclassmethod#
    def registrar(self, conta):#metod registrar para receber a conta
        pass#


class Saque(Transacao):#aki como e uma classe que vem de uma classe abstrata ela tem seguir os padroes da mesma
    def __init__(self, valor):#quando temos um valor tipo saque, temos que instanciar esse valor
        self._valor = valor#aki armazenamos no atributo valor

    @property#
    def valor(self):#aki temos acesso ao valor atraves dessa propriedade
        return self._valor#

    def registrar(self, conta):#metodo de sucesso na transação e quando ela foi efetuado
        sucesso_transacao = conta.sacar(self.valor)#

        if sucesso_transacao:#informando o sucesso e adicionando em historico da conta
            conta.historico.adicionar_transacao(self)#


class Deposito(Transacao):##aki como e uma classe que vem de uma classe abstrata ela tem seguir os padroes da mesma
    def __init__(self, valor):##quando temos um valor tipo deposito, temos que instanciar esse valor
        self._valor = valor##aki armazenamos no atributo valor

    @property#
    def valor(self):#:#aki temos acesso ao valor atraves dessa propriedade
        return self._valor#

    def registrar(self, conta):#
        sucesso_transacao = conta.depositar(self.valor)#

        if sucesso_transacao:#
            conta.historico.adicionar_transacao(self)#