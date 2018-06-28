from models.service import Service
import mlab
from faker import Faker
from random import randint,choice

mlab.connect()

fake = Faker()

# for i in range(10):
# print("Saving service", i+1, ".....")
new_service = Service(
    name="Tu Linh Thu",
    yob= 1997,
    gender=randint(0, 1),
    height=randint(155, 190),
    phone=fake.phone_number(),
    address=fake.address(),
    status=choice([True, False]),
    image = "/static/image/tulinh.jpg",
    description = "dam duc",
    measure = [50,50,50]
)

new_service.save()