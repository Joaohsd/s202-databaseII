from database import Database

class TeacherCRUD:
    def __init__(self, uri, user, password):
        self.__db = Database(uri, user, password)
    
    def create_teacher(self, name, birth_year, cpf):
        query = "CREATE (:Teacher{name:$name, birth_year:$birth_year, cpf:$cpf})"
        parameters = {"name":name, "birth_year": birth_year, "cpf":cpf}
        self.__db.execute_query(query, parameters)

    def read_teacher(self, name):
        query = "MATCH (t:Teacher{name:$name}) RETURN t.name as name, t.birth_year as birth_year, t.cpf as cpf LIMIT 1"
        parameters = {"name":name}
        results = self.__db.execute_query(query, parameters)
        if len(results) > 0:
            return [[result['name'], result['birth_year'], result['cpf']] for result in results]

    def delete_teacher(self, name):
        query = "MATCH (t:Teacher{name:$name}) DETACH DELETE t"
        parameters = {"name":name}
        self.__db.execute_query(query, parameters)

    def update_teacher(self, name, newCpf):
        query = "MATCH (t:Teacher{name:$name}) SET t.cpf = $new_cpf"
        parameters = {"name":name, "new_cpf":newCpf}
        self.__db.execute_query(query, parameters)