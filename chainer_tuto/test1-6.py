class DateManager:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def add_x(self,delta):
        self.x += delta
    def add_y(self,delta):
        self.y += delta
    def add_z(self,delta):
        self.z += delta
    def sum(self):
        return self.x + self.y + self.z

date_manager = DateManager(2,3,5)
print(date_manager.sum())
date_manager.add_x(4)
print(date_manager.sum())
date_manager.add_y(0)
print(date_manager.sum())
date_manager.add_z(-9)
print(date_manager.sum())