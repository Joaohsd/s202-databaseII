# **Contextualized Exercise**

Create a graph in Neo4J in order to list songs and albums of an artist for Spotify. In addition, this service must recommend bands that have some relation.

## **Creating nodes**
```javascript
CREATE(:Band{name:'Metallica', formed:1981, genre:'Heavy Metal'});
CREATE(:Album{name:'Black Album', released:1986, tracks:12});
CREATE(:Song{name:'Enter Sandman', duration:330});

CREATE(:Band{name:'Iron Maiden', formed:1975, genre:'Heavy Metal'});
CREATE(:Album{name:'Piece of Mind', released:1983, tracks:9});
CREATE(:Song{name:'The Trooper', duration:252});

CREATE(:Band{name:'Bon Jovi', formed:1983, genre:'Rock'});
CREATE(:Album{name:'Crush', released:2000, tracks:13});
CREATE(:Song{name:'It\'s my life', duration:225});
```

## **Creating relationships between band and albums**
```javascript
MATCH (b:Band{name:'Metallica'}),(a:Album{name:'Black Album'})
CREATE (b)-[:RECORD]->(a);
MATCH (b:Band{name:'Iron Maiden'}),(a:Album{name:'Piece of Mind'})
CREATE (b)-[:RECORD]->(a);
MATCH (b:Band{name:'Bon Jovi'}),(a:Album{name:'Crush'})
CREATE (b)-[:RECORD]->(a);
```

## **Creating relationships between albums and songs**
```javascript
MATCH (a:Album{name:'Black Album'}),(s:Song{name:'Enter Sandman'})
CREATE (a)-[:HAS]->(s);
MATCH (a:Album{name:'Piece of Mind'}),(s:Song{name:'The Trooper'})
CREATE (a)-[:HAS]->(s);
MATCH (a:Album{name:'Crush'}),(s:Song{name:'It\'s my life'})
CREATE (a)-[:HAS]->(s);
```

## **Creating relationships between bands**
```javascript
MATCH (b:Band{name:'Metallica'}),(x:Band{name:'Iron Maiden'})
CREATE (b)-[:RELATED_WITH{relation:'Strong'}]->(x);
MATCH (b:Band{name:'Iron Maiden'}),(x:Band{name:'Bon Jovi'})
CREATE (b)-[:RELATED_WITH{relation:'Medium'}]->(x);
```