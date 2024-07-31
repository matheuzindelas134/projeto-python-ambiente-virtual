import json
tasks = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tasks.append(tarefa)

def listar_tarefas():
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    for i, tarefa in enumerate(tasks):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i+1}. {tarefa['nome']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status})")

def marcar_como_concluida(indice):
    if 0 <= indice < len(tasks):
        tasks[indice]["concluida"] = True
    else:
        print("Índice inválido")

def exibir_por_prioridade(prioridade):
    encontrou = False
    for tarefa in tasks:
        if tarefa["prioridade"] == prioridade:
            encontrou = True
            print(f"{tarefa['nome']} - {tarefa['descricao']} (Categoria: {tarefa['categoria']})")
    if not encontrou:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")

def exibir_por_categoria(categoria):
    encontrou = False
    for tarefa in tasks:
        if tarefa["categoria"] == categoria:
            encontrou = True
            print(f"{tarefa['nome']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']})")
    if not encontrou:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")

def menu():
    while True:
        print("\nMenu de Gerenciamento de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir tarefas por prioridade")
        print("5. Exibir tarefas por categoria")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (baixa, média, alta): ")
            categoria = input("Categoria: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)

        elif escolha == '2':
            listar_tarefas()

        elif escolha == '3':
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
                marcar_como_concluida(indice)
            except ValueError:
                print("Por favor, digite um número válido.")

        elif escolha == '4':
            prioridade = input("Digite a prioridade (baixa, média, alta): ")
            exibir_por_prioridade(prioridade)

        elif escolha == '5':
            categoria = input("Digite a categoria: ")
            exibir_por_categoria(categoria)

        elif escolha == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()