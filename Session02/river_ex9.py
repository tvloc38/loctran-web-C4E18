from models.river import River
import river.mlab

river.mlab.connect()

river_SA_1000 = River.objects(continent = "S. America", length__lt=1000) 

for river in river_SA_1000:
    print(river.name)
    print(river.length)
    print("*" * 10)