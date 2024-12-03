# Found somewhere on the internet
import pygame as pg
import sys


# Define a class named ColorPicker
class ColorPicker(object):

    def __init__(self, screen):
        """Constructor method, initializes the ColorPicker object"""
        # Boolean flag to track if color picking is done
        self.done = False
        # Reference to the screen object
        self.screen = screen
        # Font for displaying text on the screen
        self.font = pg.font.Font("freesansbold.ttf", 16)
        # Clock object to control the frame rate
        self.clock = pg.time.Clock()
        # Frames per second for the application
        self.fps = 30

        # Size of the square representing each color
        self.square_size = 20
        # Assign the THECOLORS builtin colors to self.colors
        self.colors = pg.color.THECOLORS
        # Create a blank list for labels and color_names
        self.labels = []
        self.color_names = []
        # Variable to store the currently selected color
        self.current_color = None


# ------------------------------ DRAW ------------------------------------ #


    def draw(self, surface):
        """Method to draw the color picker on a specified surface"""
        # Fill the screen with a black color
        self.screen.fill(pg.Color("black"))
        # Size of each color square
        square_size = 20
        # Initialize left and top coordinates for drawing colors
        left = 0
        top = 0

        # Iterate through each color in self.colors
        for color in self.colors:
            # Draw a colored rectangle on the screen
            pg.draw.rect(
                self.screen,
                self.colors[color],
                (left, top, square_size, square_size)
            )
            # Update left coordinate for the next color
            left += square_size
            # Check if the next color should be drawn on a new row
            if left + square_size > surface.get_width():
                top += square_size
                left = 0

        # Iterate through each label in self.labels
        for label in self.labels:
            # Blit the label's text and position it on the surface
            surface.blit(label[0], label[1])

# ------------------------------ UPDATE ---------------------------------- #
    def update(self):
        """Method to update the labels based 
        on the current_color and color_names"""
        # Clear the existing labels list
        self.labels = []
        # Initialize left and top coordinates for label placement
        left = 0
        top = 450

        # Check if there is a current_color selected
        if self.current_color:
            # Render the RGB value of the current_color as a label
            rgb_label = self.font.render("{}".format(self.current_color),
                                         True,
                                         pg.Color("white"),
                                         pg.Color("black"))
            # Get the rectangle of the rendered label and position it
            rgb_rect = rgb_label.get_rect(topleft=(left, top))
            # Append the label and its rectangle to the labels list
            self.labels.append((rgb_label, rgb_rect))
            # Update the left coordinate for the next label
            left += rgb_rect.width + 10

        # Iterate through each color name in color_names
        for name in self.color_names:
            # Render the color name as a label
            name_text = self.font.render("{0}".format(name),
                                         True,
                                         pg.Color("white"),
                                         pg.Color("black"))
            # Get the rectangle of the rendered label and position it
            name_rect = name_text.get_rect(topleft=(left, top))
            # Update the left coordinate for the next label
            left = name_rect.right + 20
            # Append the label and its rectangle to the labels list
            self.labels.append((name_text, name_rect))

# ------------------------------ EVENT LOOP ------------------------------ #
    def event_loop(self):
        # Method to handle events in the ColorPicker application
        # Iterate through all events in the event queue
        for event in pg.event.get():
            # Check if the event is a window close (QUIT)
            if event.type == pg.QUIT:
                # Set the 'done' flag to True to exit the main loop
                self.done = True
            # Check if the event is a mouse button click
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Get the color at the mouse click position on the screen
                self.current_color = self.screen.get_at(event.pos)
                # Clear the existing color_names list
                self.color_names = []
                # Iterate through colors and find names matching the current color
                for name, value in self.colors.items():
                    if value == self.current_color:
                        # Append the matching color names to color_names list
                        self.color_names.append(name)

# ------------------------------ GAME LOOP ------------------------------- #
    def run(self):
        # Method to run the main loop of the application
        # Continue running the loop until the 'done' flag is True
        while not self.done:
            # Handle events in the event loop
            self.event_loop()
            # Update the state of the ColorPicker
            self.update()
            # Draw the ColorPicker on the screen
            self.draw(self.screen)
            # Update the display to reflect the changes
            pg.display.update()
            # Control the frame rate with the clock and specified frames per second
            self.clock.tick(self.fps)


if __name__ == "__main__":
    # Initialize Pygame
    pg.init()

    # Create a Pygame screen with dimensions 600x480
    screen = pg.display.set_mode((600, 480))

    # Set the caption for the window
    pg.display.set_caption("Color Picker")

    # Create an instance of the ColorPicker class with the specified screen
    picker = ColorPicker(screen)

    # Run the main loop of the ColorPicker application
    picker.run()

    # Quit Pygame when the application is closed
    pg.quit()

    # Exit the system
    sys.exit()
