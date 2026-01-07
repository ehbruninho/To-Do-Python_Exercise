class Tarefa:
    next_id = 1

    def __init__(self, titulo, categoria,id=None, status="Pendente"):
        if id != None or id == 0:
            self.id = id
        else: 
             self.id = Tarefa.next_id
             Tarefa.next_id += 1
        self.titulo = titulo
        self.categoria = categoria
        self.status = status
        
    def to_dict(self):
         return{
              "id" : self.id ,  
              "titulo": self.titulo,
              "categoria": self.categoria,
              "status": self.status
         }

    def print_task(self):
        return f' {self.id} | {self.titulo} | {self.categoria} | {self.status}'
    
    def up_status_task(self):
            if self.status == "Pendente":
                self.status = "Concluido"
            else:
                 self.status = "Pendente"
            return  self.status
         
