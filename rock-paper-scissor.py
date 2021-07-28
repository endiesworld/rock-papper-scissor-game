class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(
            "{name}, select rock, paper or scissor: ".format(name=self.name))
        print("{name} selects {choice}".format(
            name=self.name, choice=self.choice))


class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()

    def compareChoices(self):
        print("implement")

    def awardPoints(self):
        print("implement")


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)

    def checkEndCondition(self):
        print("implement")

    def determineWinner(self):
        print("implement")


# class Square:
#     def __init__(self, w, h):
#         self.height = h
#         self.__width = w


# def set_side(self, new_side):
#     self.__height = new_side
#     self.__width = new_side


# @property
# def height(self):
#     return self.__height


# @height.setter
# def height(self, new_value):
#     print('setting the height of your square')
#     if new_value >= 0:
#         self.__height = new_value
#     else:
#         raise Exception("Value must be larger than 0")


# mySquare = Square(5, 5)
# mySquare.set_side(10)
