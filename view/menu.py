from controller.manager import *

def menu(task_dict):
    op = 0
    
    while (op != 6):
        print("\nSeja bem vindo ao TO-DO")

        print("\n1 - Adicionar Tarefa\n" \
            "2 - Listar Tarefa \n" \
            "3 - Filtrar Tarefas por categoria\n" \
            "4 - Marcar tarefa como concluida\n" \
            "5 - Remover Tarefa\n" \
            "6 - Sair")

        op = input_validate_int("\nEscolha: ")

        if op == 1:
                    task_name = input_validate("\nNome da Tarefa: ")
                    task_category = input_validate("Categoria da tarefa: ")
                    add_task(task_dict,task_name,task_category)
                    
        if op == 2:
                    list_task(task_dict)
        if op == 3:
                    filter_task = input_validate("\nCategoria desejada: ")
                    list_filter_cat(task_dict, filter_task)
        if op == 4:
                    id_task = input_validate_int("\nDigite o ID da tarefa que deseja atualizar: ")
                    up_task(task_dict,id_task)          
        if op == 5:
                    id_task = input_validate_int("\n Digite qual ID da tarefa que deseja excluir: ")
                    remove_task(task_dict,id_task)
        
