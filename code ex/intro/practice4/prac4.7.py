# student_info.pkl contains a dumped list of students' information (already uploaded to the system). We create a copy of that file, named updated_info.pkl, to update new students.
# Write a function to add the information of a student to the dumped list in updated_info.pkl. If the student ID in that information piece has already existed in the list, overwrite all of that student's information with the new one. If the student ID is missing, do nothing.
# The content structure of the dumped list, for example:

# student_info = [
#   {
#    'id': 20200000,
#    'name': 'Nguyen Van A',
#    'score': {
#     'math': 7.8,
#     'english': 8.9,
#     'physics': 9.0,
#    }
#   },
#   {
#    'id': 20200001,
#    'name': 'Le Van B',
#    'score': {
#     'math': 9.8,
#     'english': 8.7,
#     'physics': 7.6,
#    }
#   }
# ]

# For example:

# Test	
    # new_student = {
    #         'id': 20200000,
    #         'name': 'Nguyen Van Anh',
    #         'score': {
    #             'math': 7.8,
    #             'english': 8.4,
    #             'physics': 8.0,
    #         }
    #     }
    # add_student_info(new_student)

# Result
    # Before:
    # Number of student(s): 3
    # Name of student 0: Nguyen Van An
    # After:
    # Number of student(s): 3
    # Name of student 0: Nguyen Van Anh

from shutil import copyfile
import pickle
copyfile('student_info.pkl', 'updated_info.pkl')
def add_student_info(new_student):
    with open("updated_info.pkl", "rb") as f1:
        a = pickle.load(f1)
    with open('updated_info.pkl', "wb") as f2:
        if "id" in new_student:
            x = "yet fixed"
            for i in a:
                if new_student["id"] == i["id"]:
                    a[a.index(i)] = new_student
                    x = "fixed"
                    break
            if x == "yet fixed":
                a.append(new_student)                
        pickle.dump(a, f2)
