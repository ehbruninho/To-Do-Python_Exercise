class Tarefa:
    next_id = 1

<<<<<<< HEAD
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
=======
    def __init__(self, titulo, categoria):
        self.id = Tarefa.next_id
        self.titulo = titulo
        self.categoria = categoria
        self.status = "Pendente"
        Tarefa.next_id += 1

>>>>>>> 849d99c37d4b86a35e2a809d9ea46aa331779006

    def print_task(self):
        return f' {self.id} | {self.titulo} | {self.categoria} | {self.status}'
    
    def up_status_task(self):
            if self.status == "Pendente":
                self.status = "Concluido"
            else:
                 self.status = "Pendente"
            return  self.status
         
