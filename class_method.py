# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def chk_age(self):
#         if ( self.age <= 18):
#             print("minor")
#             return
#         print("Adult")
#
#
# st1 = Student('san', 112)
# st1.chk_age()
#
#



def chk_age(name, age):
    if age <= 18:
        print("name {} , minor {}".format(name, age))
    else:
        print("name {} , adult {}".format(name, age))

chk_age('san', 1)
chk_age('san', 111)

