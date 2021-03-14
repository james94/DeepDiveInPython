class PacmanType:
    def __init__(self, playerName):
        self.score = 0
        self.pizza = 1
        self.pineapple = 5
        # Below add an attribute for ghost, make it set to 'no'

    def eat(self, dots):
        # "Below add an elif condition for a ghost. How would that affect the score?"
        if(dots.lower() == "pizza"):
            self.score = self.score + self.pizza
        elif(dots.lower() == "pineapple"):
            self.score = self.score + self.pineapple
        else:
            self.score = 0

    def up(self, movement):
        self.direction = movement
        print(self.direction)

    def down(self, movement):
        self.direction = movement

    def left(self, movement):
        self.direction = movement

    def right(self, movement):
        self.direction = movement

    def get_score(self):
        return self.score

    def get_direction(self):
        return self.direction

if __name__ == "__main__":
    name = input("Enter your name: ")
    food = input("What food does pacman eat (Hint. Pizza, Pineapple)? ")
    pacman = PacmanType(name)
    q = "no"
    play = input("Press 'p' To Play: ")
    if play.lower() == 'p':
        while(q.lower() != "yes"):
            movement = input("Move Up (w), Down (s), Left(a), Right(d):")
            if movement == 'w':
                pacman.up(movement)
                pacman.eat(food)
            elif movement == 's':
                pacman.down(movement)
                pacman.eat(food)
            elif movement == 'a':
                pacman.left(movement)
                pacman.eat(food)
            elif movement == 'd':
                pacman.down(movement)
                pacman.eat(food)
            else:
                print("Movement entered is invalid. Try again.")
            print("Pacman is moving = ", pacman.get_direction())
            print("Pacman's score = ", pacman.get_score())
            q = input("Do you want to exit? Type 'yes' or 'no'")
            