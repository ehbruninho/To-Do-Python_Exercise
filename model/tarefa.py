class Tarefa:
    next_id = 1

    def __init__(self, titulo, categoria):
        self.id = Tarefa.next_id
        self.titulo = titulo
        self.categoria = categoria
        self.status = "Pendente"
        Tarefa.next_id += 1


    def print_task(self):
        return f' {self.id} | {self.titulo} | {self.categoria} | {self.status}'
    
    def up_status_task(self):
            if self.status == "Pendente":
                self.status = "Concluido"
            else:
                 self.status = "Pendente"
            return  self.status
         
