from mongoengine import *

#1. Design Database
class Service(Document):    #ten class chu cai dau viet hoa     #class: khuôn     #class(Kế thừa)
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = StringField()
    description = StringField()
    measure = StringField()

# #2. 
# new_service = Service(
#     name="Fangqing",
#     yob=2000,
#     gender=0,
#     height=160,
#     phone="0123456789123",
#     address="Sai Gon",
#     status=False
# )

# new_service.save()