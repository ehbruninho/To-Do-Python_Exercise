# 📝 Sistema de Gestão de Tarefas (To-Do) em Python

Projeto desenvolvido como parte de um **desafio de lógica e programação em Python (Nível 3)**, com foco em organização de código, Programação Orientada a Objetos (POO), validações e fluxo de execução limpo.

---

## 🎯 Objetivo do Desafio

Criar um sistema simples de gerenciamento de tarefas (To-Do), executado via terminal, **sem uso de banco de dados**, com todas as informações mantidas em memória durante a execução do programa.

O desafio busca testar:
- Lógica de programação
- Modularização
- Uso de classes e objetos
- Validações de entrada
- Controle de fluxo com menu interativo

---

## 🛠️ Funcionalidades

O sistema possui um menu em loop com as seguintes opções:

1. Adicionar tarefa  
2. Listar tarefas  
3. Filtrar tarefas por categoria  
4. Marcar tarefa como concluída  
5. Remover tarefa  
6. Sair  

---

## 📌 Regras de Negócio

### ➕ Adicionar tarefa
- O usuário informa:
  - Título
  - Categoria
- Valida se os campos não estão vazios
- Gera um **ID único incremental**
- Evita duplicidade de tarefas com mesmo título e categoria

### 📋 Listar tarefas
Formato de exibição:

ID | Título | Categoria | Status


### 🔍 Filtrar por categoria
- Exibe apenas tarefas da categoria informada
- Caso não encontre, informa o usuário

### ✅ Marcar como concluída
- Usuário informa o ID
- Valida se a tarefa existe
- Alterna o status entre **Pendente** e **Concluído**

### ❌ Remover tarefa
- Usuário informa o ID
- Valida existência
- Remove a tarefa da lista

---

## 🧱 Estrutura do Projeto


<img width="395" height="82" alt="image" src="https://github.com/user-attachments/assets/f044c807-7b98-48cf-975c-c88a6dd63193" />


---

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (POO)
- Listas e objetos em memória
- Funções bem definidas e separadas
- Validação de entrada do usuário
- Controle de fluxo com menu em loop
- Organização e legibilidade de código

---

## 🚀 Como Executar

1. Clone o repositório
2. Certifique-se de ter o Python 3 instalado
3. Execute o arquivo principal:

```bash
python menu.py

👨‍💻 Autor

Projeto desenvolvido por Bruno, estudante de Sistemas de Informação, com foco em evolução prática em Python e desenvolvimento de software.
