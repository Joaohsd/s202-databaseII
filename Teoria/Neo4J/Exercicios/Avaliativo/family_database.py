from database import Database

class FamilyDB:
    def __init__(self, database:Database):
        self.__db = database

    def create_family(self):
        # Creating relatives
        self.__create_relatives()
        # Creating pets
        self.__create_pets()
        # Creating relationships
        self.__create_relationships()        

    def __create_relatives(self):
        self.__create_me()
        self.__create_parents()
        self.__create_siblings()
        self.__create_uncles()
        self.__create_aunts()
        self.__create_cousins()
        self.__create_grandparents()
        self.__create_nephews()
        self.__create_brothers_in_law()

    def __create_relationships(self):
        self.__create_sons_relationships()
        self.__create_brothers_relationships()
        self.__create_aunts_relationships()
        self.__create_uncles_relationships()
        self.__create_grandparents_relationships()
        self.__create_cousins_relationships()
        self.__create_marriages_relationships()
        self.__create_owner_relationships()

    def __create_me(self):
        me_query = "CREATE (:Person:Student{name:\"João\",age:22,gender:\"M\"})"
        self.__db.execute_query(me_query)

    def __create_parents(self):
        mother_query = "CREATE (:Person:Secretary{name:\"Rita\",age:46,gender:\"F\"})"
        self.__db.execute_query(mother_query)
        dad_query = "CREATE (:Person:Technician{name:\"Djalma\",age:42,gender:\"M\"})"
        self.__db.execute_query(dad_query)
    
    def __create_siblings(self):
        sister_query = "CREATE (:Person:Engineer{name:\"Nayara\",age:26,gender:\"F\"})"
        self.__db.execute_query(sister_query)

    def __create_uncles(self):
        uncle_query = "CREATE (:Person:Technician{name:\"Marcos\",age:60,gender:\"M\"})"
        self.__db.execute_query(uncle_query)
        uncle_query = "CREATE (:Person:Farmer{name:\"Diomar\",age:71,gender:\"M\"})"
        self.__db.execute_query(uncle_query)
        uncle_query = "CREATE (:Person:Administrator{name:\"Fernando\",age:60,gender:\"M\"})"
        self.__db.execute_query(uncle_query)

    def __create_aunts(self):
        aunt_query = "CREATE (:Person:Administrator{name:\"Edely\",age:57,gender:\"F\"})"
        self.__db.execute_query(aunt_query)
        aunt_query = "CREATE (:Person:Administrator{name:\"Rosely\",age:55,gender:\"F\"})"
        self.__db.execute_query(aunt_query)
        aunt_query = "CREATE (:Person:Administrator{name:\"Lucia\",age:67,gender:\"F\"})"
        self.__db.execute_query(aunt_query)

    def __create_cousins(self):
        cousin_query = "CREATE (:Person:Student{name:\"Isadora\",age:22,gender:\"F\"})"
        self.__db.execute_query(cousin_query)
        cousin_query = "CREATE (:Person:Student{name:\"Luisa\",age:16,gender:\"F\"})"
        self.__db.execute_query(cousin_query)
        cousin_query = "CREATE (:Person:Student{name:\"Fredy\",age:14,gender:\"F\"})"
        self.__db.execute_query(cousin_query)
        cousin_query = "CREATE (:Person:Engineer{name:\"Rodrigo\",age:30,gender:\"M\"})"
        self.__db.execute_query(cousin_query)
    
    def __create_grandparents(self):
        grandparent_query = "CREATE (:Person:Administrator{name:\"Luzia\",age:87,gender:\"F\"})"
        self.__db.execute_query(grandparent_query)
        grandparent_query = "CREATE (:Person:Administrator{name:\"João Batista\",age:85,gender:\"M\"})"
        self.__db.execute_query(grandparent_query)

    def __create_nephews(self):
        nephew_query = "CREATE (:Person:Student{name:\"Gabriel\",age:8,gender:\"M\"})"
        self.__db.execute_query(nephew_query)
    
    def __create_brothers_in_law(self):
        brother_in_law_query = "CREATE (:Person:Engineer{name:\"Pedro\",age:32,gender:\"M\"})"
        self.__db.execute_query(brother_in_law_query)

    def __create_pets(self):
        pet_query = "CREATE (:Pet:Dog{name:\"Scooby\",age:4,gender:\"M\"})"
        self.__db.execute_query(pet_query)
    
    def __create_sons_relationships(self):
        self.__create_son_relationship("João", "Rita", "Djalma")
        self.__create_son_relationship("Nayara", "Rita", "Djalma")

        self.__create_son_relationship("Gabriel", "Nayara", "Pedro")

        self.__create_son_relationship("Isadora", "Edely", "Marcos")
        self.__create_son_relationship("Luisa", "Edely", "Marcos")

        self.__create_son_relationship("Fredy", "Rosely", "Fernando")

        self.__create_son_relationship("Djalma", "Luzia", "João Batista")
        self.__create_son_relationship("Edely", "Luzia", "João Batista")
        self.__create_son_relationship("Rosely", "Luzia", "João Batista")

    def __create_brothers_relationships(self):
        self.__create_sibling_relationship("João", "Nayara")

        self.__create_sibling_relationship("Djalma", "Edely")
        self.__create_sibling_relationship("Djalma", "Rosely")
        self.__create_sibling_relationship("Rosely", "Edely")

        self.__create_sibling_relationship("Isadora", "Luisa")

    def __create_aunts_relationships(self):
        self.__create_aunt_relationship("Rita", "Isadora")
        self.__create_aunt_relationship("Rita", "Luisa")
        self.__create_aunt_relationship("Rita", "Fredy")
        self.__create_aunt_relationship("Rita", "Rodrigo")

        self.__create_aunt_relationship("Edely", "João")
        self.__create_aunt_relationship("Edely", "Nayara")
        self.__create_aunt_relationship("Edely", "Fredy")

        self.__create_aunt_relationship("Rosely", "João")
        self.__create_aunt_relationship("Rosely", "Nayara")
        self.__create_aunt_relationship("Rosely", "Isadora")
        self.__create_aunt_relationship("Rosely", "Luisa")

        self.__create_aunt_relationship("Lucia", "João")
        self.__create_aunt_relationship("Lucia", "Nayara")
        self.__create_aunt_relationship("Lucia", "Rodrigo")
    
    def __create_uncles_relationships(self):
        self.__create_uncle_relationship("Djalma", "Isadora")
        self.__create_uncle_relationship("Djalma", "Luisa")
        self.__create_uncle_relationship("Djalma", "Rodrigo")

        self.__create_uncle_relationship("Marcos", "João")
        self.__create_uncle_relationship("Marcos", "Nayara")
        self.__create_uncle_relationship("Marcos", "Fredy")

        self.__create_uncle_relationship("Fernando", "João")
        self.__create_uncle_relationship("Fernando", "Nayara")
        self.__create_uncle_relationship("Fernando", "Isadora")
        self.__create_uncle_relationship("Fernando", "Luisa")

        self.__create_uncle_relationship("Diomar", "João")
        self.__create_uncle_relationship("Diomar", "Nayara")
        self.__create_uncle_relationship("Diomar", "Rodrigo")

        self.__create_uncle_relationship("João", "Gabriel")

    def __create_grandparents_relationships(self):
        self.__create_grandparent_relationship("João Batista", "João")
        self.__create_grandparent_relationship("João Batista", "Nayara")
        self.__create_grandparent_relationship("João Batista", "Isadora")
        self.__create_grandparent_relationship("João Batista", "Luisa")
        self.__create_grandparent_relationship("João Batista", "Fredy")

        self.__create_grandparent_relationship("Luzia", "João")
        self.__create_grandparent_relationship("Luzia", "Nayara")
        self.__create_grandparent_relationship("Luzia", "Isadora")
        self.__create_grandparent_relationship("Luzia", "Luisa")
        self.__create_grandparent_relationship("Luzia", "Fredy")

    def __create_cousins_relationships(self):
        self.__create_cousin_relationship("João", "Isadora")
        self.__create_cousin_relationship("João", "Luisa")
        self.__create_cousin_relationship("João", "Fredy")
        self.__create_cousin_relationship("João", "Rodrigo")

        self.__create_cousin_relationship("Nayara", "Isadora")
        self.__create_cousin_relationship("Nayara", "Luisa")
        self.__create_cousin_relationship("Nayara", "Fredy")
        self.__create_cousin_relationship("Nayara", "Rodrigo")

        self.__create_cousin_relationship("Isadora", "Fredy")

        self.__create_cousin_relationship("Luisa", "Fredy")
    
    def __create_marriages_relationships(self):
        self.__create_marriage_relationship("Rita", "Djalma")
        self.__create_marriage_relationship("Nayara", "Pedro")
        self.__create_marriage_relationship("Luzia", "João Batista")
        self.__create_marriage_relationship("Edely", "Marcos")
        self.__create_marriage_relationship("Lucia", "Diomar")
    
    def __create_owner_relationships(self):
        self.__create_owner_relationship("Marcos", "Scooby", 2018)
        self.__create_owner_relationship("Edely", "Scooby", 2018)

    def __create_son_relationship(self, child_name, mother_name, father_name):
        query = "MATCH (s:Person{name:$child_name}),(m:Person{name:$mother_name}),(d:Person{name:$father_name}) CREATE (s)-[:CHILD_OF]->(m),(s)-[:CHILD_OF]->(d)"
        parameters = {"child_name": child_name, "mother_name":mother_name, "father_name":father_name}
        self.__db.execute_query(query, parameters)

    def __create_sibling_relationship(self, first_sibling_name, second_sibling_name):
        query = "MATCH (s:Person{name:$first_sibling}),(m:Person{name:$second_sibling}) CREATE (s)-[:SIBLING_OF]->(m)"
        parameters = {"first_sibling": first_sibling_name, "second_sibling": second_sibling_name}
        self.__db.execute_query(query, parameters)

    def __create_aunt_relationship(self, aunt_name, nephew_name):
        query = "MATCH (s:Person{name:$aunt}),(m:Person{name:$nephew}) CREATE (s)-[:AUNT_OF]->(m)"
        parameters = {"aunt": aunt_name, "nephew": nephew_name}
        self.__db.execute_query(query, parameters)

    def __create_uncle_relationship(self, uncle_name, nephew_name):
        query = "MATCH (s:Person{name:$uncle}),(m:Person{name:$nephew}) CREATE (s)-[:UNCLE_OF]->(m)"
        parameters = {"uncle": uncle_name, "nephew": nephew_name}
        self.__db.execute_query(query, parameters)

    def __create_grandparent_relationship(self, grandparent_name, grandchild_name):
        query = "MATCH (s:Person{name:$grandparent}),(m:Person{name:$grandchild}) CREATE (s)-[:GRANDPARENT_OF]->(m)"
        parameters = {"grandparent": grandparent_name, "grandchild": grandchild_name}
        self.__db.execute_query(query, parameters)
    
    def __create_cousin_relationship(self, first_cousin_name, second_cousin_name):
        query = "MATCH (s:Person{name:$first_cousin}),(m:Person{name:$second_cousin}) CREATE (s)-[:COUSIN_OF]->(m)"
        parameters = {"first_cousin": first_cousin_name, "second_cousin": second_cousin_name}
        self.__db.execute_query(query, parameters)

    def __create_marriage_relationship(self, wife_name, husband_name):
        query = "MATCH (w:Person{name:$wife_name}), (h:Person{name:$husband_name}) CREATE (w)-[:MARRIED_TO]->(h)"
        parameters = {"wife_name": wife_name, "husband_name": husband_name}
        self.__db.execute_query(query, parameters)
    
    def __create_owner_relationship(self, owner_name, pet_name, year):
        query = "MATCH (o:Person{name:$owner_name}), (p:Pet{name:$pet_name}) CREATE (o)-[:OWNER_OF{since:$year}]->(p)"
        parameters = {"owner_name": owner_name, "pet_name": pet_name, "year": year}
        self.__db.execute_query(query, parameters)

    def get_engineers(self):
        '''
            This method returns a list of list with information about engineers in family
        '''
        query = "MATCH (e:Engineer) RETURN e.name AS name, e.age AS age, e.gender AS gender ORDER BY e.age"
        results = self.__db.execute_query(query)
        if len(results) > 0:
            return [[result['name'], result['age'], result['gender']] for result in results]
        
    def get_students(self):
        '''
            This method returns a list of list with information about students in family
        '''
        query = "MATCH (s:Student) RETURN s.name AS name, s.age AS age, s.gender AS gender ORDER BY s.age"
        results = self.__db.execute_query(query)
        if len(results) > 0:
            return [[result['name'], result['age'], result['gender']] for result in results]

    def get_marriages_relatioships(self):
        '''
            This method returns a list of list with married couples in family
        '''
        query = "MATCH (p:Person)-[m:MARRIED_TO]->(pp:Person) RETURN p.name AS wife_name, pp.name AS husband_name"
        results = self.__db.execute_query(query)
        if len(results) > 0:
            return [[result['wife_name'], result['husband_name']] for result in results]
        
    def get_children_of_person(self, parent_name):
        '''
            This method returns children's name of given 'parent_name' person
        '''
        query = "MATCH (p:Person)-[:CHILD_OF]->(pp:Person{name:$parent_name}) RETURN p.name AS child_name"
        parameters = {"parent_name": parent_name}
        results = self.__db.execute_query(query, parameters)
        if len(results) > 0:
            return [result['child_name'] for result in results]

        
