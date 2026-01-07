import json
import os
from model.tarefa import Tarefa


def save_archive(dict_task):
    with open ("task.json", "w",encoding="utf-8") as file:
        json.dump(dict_task,file, indent=4)

def load_archive():
    with open("task.json","r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def exist_archive()-> bool:
    archive = "task.json"
    if os.path.exists(archive):
        return True
    return False
   
def convert_json_obj() -> dict:
    data = load_archive()
    task_obj = {}
    ids_tasks = []
    max_id = 0

    for task_id, task_value in data.items():
        task_obj[int(task_id)] = Tarefa(task_value['id'],task_value['titulo'], task_value['categoria'],task_value['status'])
        ids_tasks.append(int(task_id))
    
    if data:
        max_id = max(ids_tasks)

    next_id = max_id + 1
    Tarefa.next_id = next_id
    
    return task_obj

def convert_dict_json(dict_task:dict) -> dict:
     new_dict_task = {}
     for id_task, obj_task in dict_task.items():
          new_dict_task[id_task] = obj_task.to_dict()
     save_archive(new_dict_task)
     return new_dict_task