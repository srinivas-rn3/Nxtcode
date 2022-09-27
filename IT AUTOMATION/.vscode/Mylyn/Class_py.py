class Human:
    def __init__(self,n,o):
      self.name = n
      self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"Plays Tennis")
        elif self.occupation == "actor":
            print(self.name,"Shoot a film")

    def speaks(self):
        print(self.name,"Say How Are you?")
tom = Human("Tom Cruise","actor")
tom.do_work()
tom.speaks()
maria = Human("Maria Sharpova", "tennis player")
maria.do_work()
maria.speaks()