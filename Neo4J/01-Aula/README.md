# **Exercise**

## **Question 1**

### **ITEM 1**

```javascript
MATCH (nodes) RETURN nodes
```

### **ITEM 2**

```javascript
MATCH (g:Game) WHERE g.ano > 2012 RETURN g
```

### **ITEM 3**

```javascript
MATCH (g:Game) WHERE g.genero = 'Terror' RETURN g
```

### **ITEM 3**

```javascript
MATCH (j:Jurado)-[r:JOGOU]->(g:Game) WHERE r.nota >=7 RETURN g
```

## **Question 2**

### **ITEM 1**
```javascript
CREATE(g:Game{titulo:'God of War 3',genero:'Acão',ano:2010});
CREATE(g:Game{titulo:'League of Legends',genero:'RPG',ano:2009});
CREATE(g:Game{titulo:'Need for Speed: Underground 2',genero:'Corrida',ano:2004});
CREATE(g:Game{titulo:'Resident Evil 6',genero:'Survival Horror',ano:2012});
```

### **ITEM 2**
```javascript
CREATE(j:Jurado{nome:'João'});
CREATE(j:Jurado{nome:'Maria'});
CREATE(j:Jurado{nome:'Pedro'});
```

### **ITEM 3**
```javascript
MATCH(j:Jurado{nome:'João'}),(g:Game{titulo:'God of War 3'})
CREATE(j)-[:JOGOU{nota:8.5, horas:200}]->(g);

MATCH(j:Jurado{nome:'Maria'}),(g:Game{titulo:'League of Legends'})
CREATE(j)-[:JOGOU{nota:10, horas: 2000}]->(g);

MATCH(j:Jurado{nome:'Pedro'}),(g:Game{titulo:'Need for Speed: Underground 2'})
CREATE(j)-[:JOGOU{nota:6, horas: 135}]->(g);

MATCH(j:Jurado{nome:'João'}),(g:Game{titulo:'Resident Evil 6'})
CREATE(j)-[:JOGOU{nota:4, horas: 30}]->(g);
```