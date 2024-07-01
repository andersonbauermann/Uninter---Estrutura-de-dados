# Exercício 1: Lista Encadeada

## Enunciado
Um hospital deseja informatizar seu sistema de triagem para priorizar atendimentos. Pacientes recebem cartões amarelos (A) para casos urgentes e cartões verdes (V) para casos menos urgentes. A prioridade de atendimento segue estas regras:
- Pacientes com cartão amarelo (A) são atendidos antes dos com cartão verde (V).
- Entre pacientes com a mesma cor, os com numeração menor são atendidos antes.
- Numerações: Amarelo inicia em 201 e Verde em 1.

### Implementações Requeridas
1. **Lista Encadeada Simples:**
   - Nodo com número, cor e ponteiro para o próximo.
   - Ponteiro para a cabeça da lista (head).
2. **Função `inserirSemPrioridade(nodo)`:**
   - Insere o nodo no final da lista.
3. **Função `inserirComPrioridade(nodo)`:**
   - Insere o nodo após todos os nodos com cor “A” na lista.
4. **Função `inserir()`:**
   - Solicita cor e número ao usuário.
   - Cria um nodo e insere conforme a cor: 
     - Lista vazia: head aponta para o nodo.
     - Cor "V": chama `inserirSemPrioridade(nodo)`.
     - Cor "A": chama `inserirComPrioridade(nodo)`.
5. **Função `imprimirListaEspera()`:**
   - Imprime todos os cartões e números da lista.
6. **Função `atenderPaciente()`:**
   - Remove o primeiro paciente da lista e informa o número do cartão.
7. **Menu do Sistema:**
   - Opções: adicionar paciente (1), mostrar pacientes (2), chamar paciente (3), sair (4).

### Testes Requeridos
1. Inserir três pacientes com cartão "V", dois com cartão "A", dois com cartão "V" e três com cartão "A" (nessa ordem).
2. Imprimir a lista de espera.
3. Atender dois pacientes e imprimir a lista novamente.

# Exercício 2: Tabela Hash

## Enunciado
Desenvolver uma tabela hash para emplacamento de veículos, onde o último número da placa representa o estado de registro. A tabela possui 10 posições (0-9), e a função hash segue estas regras:
- Entrada: string com 2 letras (sigla do estado).
- Sigla "DF" retorna 7.
- Outros: soma dos valores ASCII das letras, módulo 10.

### Implementações Requeridas
1. **Tabela Hash:**
   - 10 posições inicializadas como `None`.
2. **Lista Encadeada Simples:**
   - Nodo com sigla, nome do estado e ponteiro para o próximo.
   - Cabeça de cada lista aponta para `None`.
3. **Inserção no Início da Lista:**
   - Novo elemento é inserido no início da lista.
4. **Impressão da Tabela Hash:**
   - Imprime as siglas de todos os nodos em cada posição.
5. **Função Hash:**
   - Conforme as regras especificadas.
6. **Inserção dos Estados:**
   - Inserir os 26 estados e o Distrito Federal na tabela.
7. **Estado Fictício:**
   - Inserir um estado fictício com sigla e nome completo.

### Testes Requeridos
1. Imprimir a tabela hash antes de inserir qualquer informação.
2. Imprimir a tabela após inserir os 26 estados e o Distrito Federal.
3. Imprimir a tabela após inserir os 26 estados, o Distrito Federal e o estado fictício.
