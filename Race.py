from graphics import *
from Dice import *

# Horse class: Shows each horse in the race (Position, Movement, Drawing)
class Horse:
    def __init__(self, speed, y, image, window):
        self.x = 40
        self.y = y
        self.image = image
        self.window = window
        self.dice = Dice(speed)

    def draw(self):
        self.image.draw_at_pos(self.window, self.x, self.y)

    # Move horse by dice roll
    def move(self):
        roll_value = self.dice.roll()
        self.x = self.x + roll_value
        self.image.move(roll_value, 0)

    # Check horse cross line
    def crossed_finish_line(self, finish_x):
        return self.x >= finish_x


def main():
        win = GraphWin("Horse Race", 700, 350)

        # Create horse images
        img1 = Image(Point(0, 0), "CharacterRun1.gif")
        img2 = Image(Point(0, 0), "CharacterRun2.gif")
        img3 = Image(Point(0, 0), "CharacterRun3.gif")

        # Initialize horses at different y positions
        horse1 = Horse(6,80, img1, win)
        horse2 = Horse(6, 150, img2, win)
        horse3 = Horse(6, 220, img3, win)

        # Draw horses
        horse1.draw()
        horse2.draw()
        horse3.draw()

        # Draw finish line
        finish_x = 600
        finish_line = Line(Point(finish_x, 0), Point(finish_x, 350))
        finish_line.draw(win)

        win.getMouse()  # User click to start the race

        race_over = False

        while not race_over:
            # Move all horses on each frame
            horse1.move()
            horse2.move()
            horse3.move()
            update(60)

            # Check if any horse crossed the finish line
            if (horse1.crossed_finish_line(finish_x) or
                horse2.crossed_finish_line(finish_x) or
                horse3.crossed_finish_line(finish_x)):
                race_over = True

        # Determine Winner
        h1 = horse1.crossed_finish_line(finish_x)
        h2 = horse2.crossed_finish_line(finish_x)
        h3 = horse3.crossed_finish_line(finish_x)

        # Text out, which horse win the race or tie
        if h1 and not h2 and not h3:
            winner_text = Text(Point(350, 35), "Horse Race winner is H1!")
        elif h2 and not h1 and not h3:
            winner_text = Text(Point(350, 35), "Horse Race winner is H2!")
        elif h3 and not h1 and not h2:
            winner_text = Text(Point(350, 35), "Horse Race winner is H3!")
        else:
            winner_text = Text(Point(350, 35), "It's a tie!")

        # Close the window if click
        winner_text.draw(win)
        win.getMouse()
        win.close()

if __name__ == '__main__':
    main()