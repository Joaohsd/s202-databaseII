# **Second Test**

## **Nodes and Relationships**

```javascript
// Criação de usuários
CREATE (a:Usuario {nome: 'Alice', idade: 25})
CREATE (b:Usuario {nome: 'Bob', idade: 30})
CREATE (c:Usuario {nome: 'Charlie', idade: 35})
CREATE (d:Usuario {nome: 'David', idade: 40})
CREATE (e:Usuario {nome: 'Eve', idade: 45})

// Criação de postagens
CREATE (p1:Postagem {titulo: 'Observações do Amanhecer', conteudo: 'Conteúdo da Observações do Amanhecer'})
CREATE (p2:Postagem {titulo: 'Memórias da Tarde', conteudo: 'Conteúdo da Memórias da Tarde'})
CREATE (p3:Postagem {titulo: 'Segredos da Noite', conteudo: 'Segredos da Noite'})

// Definindo relações de amizade
CREATE (a)-[:AMIGO]->(b)
CREATE (b)-[:AMIGO]->(c)
CREATE (c)-[:AMIGO]->(d)
CREATE (d)-[:AMIGO]->(e)

// Definindo quem fez as postagens
CREATE (a)-[:POSTOU]->(p1)
CREATE (b)-[:POSTOU]->(p2)
CREATE (c)-[:POSTOU]->(p3)
```

## **PART 1: Search and Basic Operations**

### **Question 1**

As we just have one kind of relationship (**AMIGO**) between users, we can use "--" to identify friends of Bob.

```javascript
MATCH (b:Usuario{nome:"Bob"})--(u:Usuario) RETURN u.nome AS nome ORDER BY u.nome
```

### **Question 2**

The title of second post done was 'Memórias da Tarde', so we search for users that have posted it filtering by title propertie.

```javascript
MATCH (u:Usuario)-[:POSTOU]->(p:Postagem{titulo: 'Memórias da Tarde'}) RETURN u.nome AS nome
```

### **Question 3**

In order to find users that have posted something and are older than 35 years old, we search for users based on 'POSTOU' relationship and 'idade' propertie.

```javascript
MATCH (u:Usuario)-[:POSTOU]->(p:Postagem) WHERE u.idade > 35 RETURN u.nome AS nome
```

## **PART 2: Neo4J Operations**

### **Question 1**

In order to find the oldest user, the query was done ordering by 'idade' propertie in descending order, returning just the first one.

```javascript
MATCH (u:Usuario) RETURN u.nome as nome ORDER BY u.idade DESC LIMIT 1
```

### **Question 2**

The number of users that are older than 30 years is possible by the query below, using 'COUNT()' function:

```javascript
MATCH (u:Usuario) WHERE u.idade > 30 RETURN COUNT(*)
```

### **Question 3**

The average age of users:

```javascript
MATCH (u:Usuario) RETURN AVG(u.idade)
```
