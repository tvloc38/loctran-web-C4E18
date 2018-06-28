from models.service import Service
import mlab
from faker import Faker
from random import randint,choice

mlab.connect()

fake = Faker()

# for i in range(10):
# print("Saving service", i+1, ".....")
new_service = Service(
    name="Tu Linh",
    yob= 1994,
    gender=randint(0, 1),
    height=randint(155, 190),
    phone=fake.phone_number(),
    address=fake.address(),
    status=choice([True, False]),
    image = "/static/image/tulinh.jpg",
    description = "ngoan hien, de thuong",
    measure = "90-60-90"
)

new_service.save()