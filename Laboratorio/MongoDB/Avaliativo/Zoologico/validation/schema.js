{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      '_id',
      'nome',
      'especie',
      'idade', 
      'habitats'
    ],
    properties: {
      _id: {
        bsonType: 'string',
        description: 'Should be a string and it\'s required.'
      },
      nome: {
        bsonType: 'string',
        description: 'Should be a string and it\'s required.'
      },
      especie: {
        bsonType: 'string',
        description: 'Should be a string and it\'s required.'
      },
      idade: {
        bsonType: 'int',
        minimum: 0,
        description: 'Should be an integer and it\'s required.'
      },
      habitats: {
        bsonType: 'array',
        description: 'Should be an array and and it\'s required.',
        minItems: 1,
        items: {
          bsonType: "object",
          required: [
            '_id',
            'nome',
            'tipoAmbiente',
            'cuidador'
          ],
          properties: {
            _id: {
              bsonType: 'string',
              description: 'Should be a string and it\'s required.'
            },
            nome: {
              bsonType: 'string',
              description: 'Should be a string and it\'s required.'
            },
            tipoAmbiente: {
              bsonType: 'string',
              description: 'Should be a string and it\'s required.'
            },
            cuidador: {
              bsonType: 'object',
              description: 'Should be an object and it\'s required.',
              required: [
                '_id',
                'nome',
                'documento'
              ],
              properties: {
                _id: {
                  bsonType: 'string',
                  description: 'Should be a string and it\'s required.'
                },
                nome: {
                  bsonType: 'string',
                  description: 'Should be a string and it\'s required.'
                },
                documento: {
                  bsonType: 'string',
                  description: 'Should be a string and it\'s required.'
                }
              }
            }
          }
        }
      }
    }
  }
}