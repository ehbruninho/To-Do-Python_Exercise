from tarefa import *

def main():
    task_list = []
    menu(task_list)

def add_task(list,task_name, task_category):
            task = Tarefa(task_name,task_category)
            list.append(task)
            print("\nTarefa registrada com sucesso!") 

def list_task(list):
      if not list:
               print ("\nNenhuma tarefa registrada!")
      else:
            print("\nID | Titulo | Categoria | Status")
            for task in list:
                print(task.print_task())

def list_filter_cat(list,filter_task):
     list_with_filter = []
     for task in list:
        if filter_task == task.categoria:
            list_with_filter.append(task)

     if len(list_with_filter)>0:
          list_task(list_with_filter)
     else:
           print("\nCategoria não localizada!")
    
def up_task(list,id_task):
     found = False

     for task in list:
          if task.id == id_task:
              task.up_status_task()
              found = True
              break

     if not found:
        print("\nID não localizado") 
     else:
        print("\nTarefa atualizada com sucesso!")
          
def input_validate(strings):
     while True:
          new_string = input(strings).strip()
          if not new_string:
                print("Esse campo não deve ser vazio!")   
          else:
                return new_string
          
def input_validate_int(strings):
   while True:
         new_int = input(strings).strip()
         if not new_int:
           print("Esse campo não deve ser vazio!")
         elif new_int.isdigit():
              return int(new_int)   
         else:
                 print("\nVocê não digitou um inteiro valido, tente novamente!")

def add_dict(dict_task,task_name, task_category):
      new_task = Tarefa(task_name,task_category)
      dict_task[new_task.id] = new_task   
      return dict_task    
        
def remove_task(list, id_task):
     found = False
     list_task(list)
     for task in list:
        if id_task==task.id:
               list.remove(task)
               found = True
               break

     if not found:
           print("\nID não localizado")
     else:
           print("\nTarefa removida com sucesso!")

def exist_validate(list,task_name, task_category):
     for task in list:
          if (task_name == task.titulo) and (task_category == task.categoria) :
               return task.id           
     return False

def menu(task_list):
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
                    result_validate = exist_validate(task_list,task_name,task_category)
                    
                    if result_validate != False:
                        print("\nJá existe uma tarefa com esse titulo e categoria registrada! Deseja atualizar o status?")
                        print("\n1 - Sim\n2 - Não ")

                        resp = input_validate_int("\nEscolha: ")
                        if resp == 1:
                            up_task(task_list,result_validate)
                            
                        elif resp ==2: 
                            continue
                    else: 
                        add_task(task_list,task_name,task_category)

        if op == 2:
                    list_task(task_list)
        if op == 3:
                    filter_task = input_validate("\nCategoria desejada: ")
                    list_filter_cat(task_list, filter_task)
        if op == 4:
                    id_task = input_validate_int("\nDigite o ID da tarefa que deseja atualizar: ")
                    up_task(task_list,id_task)          
        if op == 5:
                    id_task = input_validate_int("\n Digite qual ID da tarefa que deseja excluir: ")
                    remove_task(task_list,id_task)
        
main()