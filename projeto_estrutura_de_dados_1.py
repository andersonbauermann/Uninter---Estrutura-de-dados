class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEspera:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
        numero = int(input("Digite o número do cartão: "))
        novo_nodo = Nodo(numero, cor)
        if self.head is None:
            self.head = novo_nodo
        else:
            if cor == 'V':
                self.inserirSemPrioridade(novo_nodo)
            elif cor == 'A':
                self.inserirComPrioridade(novo_nodo)
            else:
                print("Cor inválida! Por favor, insira 'A' ou 'V'.")

    def imprimirListaEspera(self):
        atual = self.head
        if atual is None:
            print("A lista está vazia.")
        else:
            while atual:
                print(f"Cartão Número: {atual.numero}, Cor: {atual.cor}")
                atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Não há nenhum paciente na fila para atendimento.")
        else:
            print(f"Chamando paciente com cartão número {self.head.numero} para atendimento.")
            self.head = self.head.proximo

def menu():
    lista_espera = ListaEspera()
    while True:
        print("\nMenu:")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            lista_espera.inserir()
        elif opcao == '2':
            lista_espera.imprimirListaEspera()
        elif opcao == '3':
            lista_espera.atenderPaciente()
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
