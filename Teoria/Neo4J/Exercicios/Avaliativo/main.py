from database import Database
from family_database import FamilyDB

first_run = True

uri = str(input("URI: "))
user = str(input("User: "))
password = str(input("Password: "))

# Create an instance of the Database class, passing the connection data to the Neo4j database.
db = Database(uri, user, password)

if first_run:
    db.drop_all()

# Creating an instance of the FamilyDB class to interact with the database.
family_db = FamilyDB(db)

# Creating the family genealogical tree.
if first_run:
    family_db.create_family()

# What are the engineers in the family?
print("Engineers:")
print(family_db.get_engineers())

# What are the students in the family?
print("Students:")
print(family_db.get_students())

# What are Rita's children?
name = "Rita"
print(f"Children of {name}:")
print(family_db.get_children_of_person(name))

# Who are the married couples in the family?
print("Couples:")
print(family_db.get_marriages_relatioships())

# Closing the connection
db.close()