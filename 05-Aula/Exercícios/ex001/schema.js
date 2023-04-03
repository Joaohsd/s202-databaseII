{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      '_id',
      'titulo',
      'autor',
      'ano',
      'preco'
    ],
    properties: {
      _id: {
        bsonType: 'int',
        minimum: 0,
        description: 'Should be an integer and it\'s required.'
      },
      titulo: {
        bsonType: 'string',
        description: 'Should be a string and it\'s required.'
      },
      autor: {
        bsonType: 'string',
        description: 'Should be a string and it\'s required.'
      },
      ano: {
        bsonType: 'int',
        minimum: 0,
        maximum: 2023,
        description: 'Should be an interger between 0 and 2023. It\'s required.'
      },
      preco: {
        bsonType: 'double',
        minimum: 0.0,
        description: 'Should be a double and and it\'s required.'
      }
    }
  }
}