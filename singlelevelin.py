class Bike:
    def start(self):
        print("Bike started")
class newBike(Bike):
    def close(self):
        print("simple inheritance")

obj=newBike()
obj.start()
obj.close()