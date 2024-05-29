import pyfiglet

def draw_welcome_jarvis():
    # Create an instance of the Figlet class
    font = pyfiglet.Figlet()

    # Generate ASCII art for the text "Ironman"
    ascii_art = font.renderText("Welcome to Jarvis : )")

    # Print the ASCII art
    print(ascii_art)
