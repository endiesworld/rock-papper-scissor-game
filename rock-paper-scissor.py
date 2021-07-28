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

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        result = self.compareChoices(p1, p2)
        print("Round resulted in a {result}".format(
            result=self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def awardPoints(self):
        print("implement")

    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def checkEndCondition(self):
        answer = input("Continue game y/n")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name=self.participant.name,
                  p1points=self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(
                name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(
                name=self.secondParticipant.name)
        print(resultString)

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()


game = Game()
game.start()

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
