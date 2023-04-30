from db.database import Database
from utils.save_json import writeToJson
from model.personModel import PersonModel

def main():
    db = Database(database="people", collection="people-info")
    personModel = PersonModel(db)
    idPerson = personModel.create_person("Fulano", 30)
    person = personModel.read_person_by_id(idPerson)
    personModel.update_person(idPerson, "Maria Silva", 35)
    personModel.delete_person(idPerson)
    person = personModel.read_person_by_id(idPerson)
    
if __name__ == "__main__":
    main()
