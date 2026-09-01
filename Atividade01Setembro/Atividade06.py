import os
os.system("cls")

lista = []
escolha = -1
tarefa = ""

while True:
    print("====MENU====")
    print("1- Adicionar tarefa")
    print("2- Remover tarefas")
    print("3- Mostrar tarefas")
    print("0- Sair")
    
    escolha = int(input("Digite o número de uma das opções:\n"))
    
    if escolha == 1:
        tarefa = input("Digite a tarefa a ser adicionada:\n")
        lista.append(tarefa)
        print("\n\nItem cadastrado\n\n")
    elif escolha == 2:
        tarefa = input("digite a tarefa a ser removida:\n")
        if lista.count(tarefa)<1:
            print("\n\nNão há tarefa com este nome na lista.\n\n")
        else:
            lista.remove(tarefa)
            print("\n\nItem removido\n\n")
    elif escolha == 3:
        if len(lista) == 0:
            print("\n\nAinda não há tarefas cadastradas\n\n")
        else:
            for i in range(len(lista)):
                print(f"{i+1} - {lista[i]}")
    elif escolha == 0:
        print("Saindo")
        break
    else:
        print("Opção inválida")        
        
