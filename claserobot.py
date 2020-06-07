class Robot:
    Autonomy = "artificial intelligence"

    def __init__(self, name, movement, life):
        self.name = name
        self.movement = movement
        self.life = life

    def rolrobot(self):
        if self.movement == "cylindricals":
            print(self.name, "this is a robot hunter")
        elif self.movement == "polars":
            print(self.name, "this is a robot explorer")

    def utility(self):
        if self.life > 10:
            print(self.name, "robot life is extensive")
        else:
            print(self.name, "robot life is small")


robot1 = Robot("t-800", "polars", 12)
robot2 = Robot("t-1000", "cylindricals", 8)
print(robot1.name)
print(robot2.name)
robot1.rolrobot()
robot1.utility()
robot2.rolrobot()
robot2.utility()
