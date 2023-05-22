from teacher_database import TeacherCRUD

uri = str(input('Type URI: '))
user = str(input('Type USER: '))
password = str(input('Type PASSWORD: '))

teacher_crud = TeacherCRUD(uri, user, password)

# Create
teacher_crud.create_teacher('Chris Lima', 1956, '189.052.396-66')
# Read
print(teacher_crud.read_teacher('Chris Lima'))
# Update
teacher_crud.update_teacher('Chris Lima', '162.052.777-77')
# Read
print(teacher_crud.read_teacher('Chris Lima'))