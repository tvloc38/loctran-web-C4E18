from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b2baf36aa3d1815edddd842"

id_find = Service.objects.get(id=id_to_find)
print(id_find.name)

id_find.delete()

