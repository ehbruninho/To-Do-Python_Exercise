from model.tarefa import Tarefa
<<<<<<< HEAD
from model.storage import *
=======
>>>>>>> 849d99c37d4b86a35e2a809d9ea46aa331779006

def list_task(dict_task:dict) -> dict:
    if dict_task:
        print("\nID  |  Titulo  |  Categoria  |  Status")
        
        for task in dict_task.values():
            print(f'{task.id}  |  {task.titulo}  |  {task.categoria}  |  {task.status}')
<<<<<<< HEAD
=======
>>>>>>> 849d99c37d4b86a35e2a809d9ea46aa331779006
    else:
        print("\nNenhuma tarefa registrada!")
    
def list_filter_cat(dict_task,filter_task):
<<<<<<< HEAD
    new_dict_task = {}
    for task in dict_task.values():
        if task.categoria == filter_task:
            new_dict_task[task.id] = task
    if len(new_dict_task)==0:
         print("\nNenhuma categoria localizada!")
    else:
         list_task(new_dict_task)
=======
    if filter_task in dict_task['categoria']:
        task = dict_task
        print(task.print_task())
    else:
        print("\nCategoria não localizada!")
>>>>>>> 849d99c37d4b86a35e2a809d9ea46aa331779006
        
def up_task(dict_task: dict,id_task:int) -> dict:
    if id_task in dict_task:
         dict_task[id_task].up_status_task()
<<<<<<< HEAD
         convert_dict_json(dict_task) 
=======
>>>>>>> 849d99c37d4b86a35e2a809d9ea46aa331779006
    else:
         print("\n ID não localizado!")
    return dict_task
            
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

def add_task(dict_task: dict,task_name: str, task_category:str) -> dict:
    result = exist_validate(dict_task,task_name,task_category)
<<<<<<< HEAD
    if not result:
        new_task = Tarefa(task_name,task_category)
        dict_task[new_task.id] = new_task  
        convert_dict_json(dict_task) 
        print("\nTarefa registrada com sucesso!")
    return dict_task   

def remove_task(dict_task: dict, id_task:int) -> dict:
    if id_task in dict_task:
        del dict_task[id_task]
        convert_dict_json(dict_task) 
=======

    if not result:
        new_task = Tarefa(task_name,task_category)
        dict_task[new_task.id] = new_task   
        print("\nTarefa registrada com sucesso!")
    return dict_task   
         
def remove_task(dict_task: dict, id_task:int) -> dict:
    if id_task in dict_task:
        del dict_task[id_task]
>>>>>>> 849d99c37d4b86a35e2a809d9ea46aa331779006
        print("\nTarefa removida com sucesso!")
    else:
        print("\nCategoria não localizada!")
    return dict_task
    

def exist_validate(dict_task: dict,task_name: str, task_category: str) -> bool:
    for task in dict_task.values():
        if task.titulo == task_name and task.categoria == task_category:
           print(f"\nTarefa já registrada com ID {task.id}!")
           return True
    return False