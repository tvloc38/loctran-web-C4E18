from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects()
first_service = all_service[0]

print(first_service.address)     #to_mongo: ca object      #trong Mongodb thay [name] thanh .name
