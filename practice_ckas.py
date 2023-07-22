class Unit:
    def __init__(self):
        print("유닛생성자")
    
class Flyable:
    def __init__(self):
        print("Flyable생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()