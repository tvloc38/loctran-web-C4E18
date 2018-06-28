from models.river import River
import river.mlab

river.mlab.connect()

river_Africa = River.objects(continent = "Africa")

for river in river_Africa:
    print(river.name)
    print(river.length)
    print("*" * 10)