class Node:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.next = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nomeEstado):
        index = self.funcao_hash(sigla)
        novo_nodo = Node(sigla, nomeEstado)
        novo_nodo.next = self.tabela[index]
        self.tabela[index] = novo_nodo

    def imprimir_tabela(self):
        for i in range(len(self.tabela)):
            print(f"Posição {i}: ", end="")
            current = self.tabela[i]
            while current is not None:
                print(f"{current.sigla} -> ", end="")
                current = current.next
            print("None")

def main():
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    tabela_hash = TabelaHash()
    tabela_hash.imprimir_tabela()
    print("------------------------------------------------------")

    for sigla, nome in estados:
        tabela_hash.inserir(sigla, nome)

    tabela_hash.imprimir_tabela()
    tabela_hash.inserir("AB", "Anderson Bauermann")
    print("------------------------------------------------------")

    tabela_hash.imprimir_tabela()

main()
