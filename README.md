---

## 🔄 Evolução do Projeto

Este projeto faz parte de uma sequência de desafios práticos em Python, com aumento progressivo de complexidade e maturidade de código.

### 🧩 Nível 3 – Sistema de Tarefas em Memória
Versão inicial do projeto, com foco em lógica e Programação Orientada a Objetos.

**Características:**
- Execução via terminal
- Dados mantidos apenas em memória
- Estrutura simples com listas e objetos
- Menu interativo em loop

> ⚠️ Ao encerrar o programa, todas as tarefas eram perdidas.

---

### 🚀 Nível 4 – Sistema de Tarefas com Persistência (Versão Atual)

Evolução direta do projeto, agora com foco em **organização de responsabilidades e persistência de dados**, simulando um fluxo mais próximo de aplicações reais.

#### 🎯 Objetivos do Nível 4
- Manter estado entre execuções
- Separar melhor as responsabilidades do sistema
- Criar um código mais organizado e sustentável
- Garantir que os dados sobrevivam ao fechamento do programa

#### 📦 Novo Conceito Central
Persistência de dados em arquivo **JSON**.

- Ao iniciar o programa:
  - Se o arquivo existir → carrega as tarefas
  - Se não existir → inicia vazio
- Ao adicionar, remover ou atualizar:
  - Os dados são salvos automaticamente no arquivo

> 📌 Não é banco de dados. É persistência em arquivo.

#### 🧱 Separação de Responsabilidades
O projeto passa a ter papéis bem definidos:

- **Camada de Dados**
  - Carregar tarefas do arquivo JSON
  - Salvar tarefas no arquivo

- **Camada de Regras**
  - Adicionar tarefas
  - Remover tarefas
  - Atualizar status
  - Validar existência

- **Interface (Menu)**
  - Interagir com o usuário
  - Exibir mensagens
  - Chamar as regras do sistema

> O menu **não manipula diretamente** listas ou dicionários.

#### 📌 Estrutura da Tarefa
A classe `Tarefa` foi mantida, contendo:
- id
- título
- categoria
- status

Além disso, foi implementada a conversão:
- Objeto → JSON (para salvar)
- JSON → Objeto (para carregar)

#### ✅ Funcionalidades
- Adicionar tarefa
- Listar tarefas
- Filtrar por categoria
- Marcar como concluída
- Remover tarefa
- Persistência automática em arquivo
