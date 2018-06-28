from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]

# print(first_service.address)     #to_mongo: ca object      #trong Mongodb thay [name] thanh .name

id_to_find = '5b2ba3f9aa3d1812ca66380b'

hera = Service.objects.get(id=id_to_find)
# hera = Service.objects().with_id(id_to_find)



print(hera.id)

# hera.update(set__yob=2002)
# hera.reload()

# print(hera.yob)
