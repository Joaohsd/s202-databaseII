## Aggregations

```javascript
MATCH (c:CreditCard) RETURN AVG(c.limit)
```

```javascript
MATCH (b:BankAccount) RETURN COUNT(*)
```

```javascript
MATCH (m:MoneyTransfer) RETURN MIN(m.amount)
```

```javascript
MATCH (m:MoneyTransfer) RETURN MAX(m.amount)
```

```javascript
MATCH (c:CreditCard) RETURN COLLECT(c.balance)
```

## Mathematical functions

```javascript
MATCH (c:CreditCard) RETURN FLOOR(c.balance)
```

```javascript
MATCH (c:CreditCard) RETURN CEIL(c.balance)
```

```javascript
MATCH (b:BankAccount) RETURN SIGN(b.balance)
```

```javascript
MATCH (b:BankAccount) RETURN ROUND(b.balance, 1, 'CEILING')
```

```javascript
MATCH (b:BankAccount) RETURN ROUND(b.balance)
```

## String functions


```javascript
MATCH (a:AccountHolder) RETURN LEFT(a.firstName, 1)
```

```javascript
MATCH (d:DeliveryAddress) RETURN SPLIT(d.streetAddress, ' ')
```

```javascript
MATCH (a:Address) RETURN SUBSTRING(a.zip, 0, 3)
```

```javascript
MATCH (a:AccountHolder) RETURN TOUPPER(a.fullName)
```

```javascript
MATCH (c:CreditCard) RETURN RIGHT(c.expirationDate, 2)
```