from PIL import Image
import keyboard
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load the sound
coolsound = pygame.mixer.Sound("content/coolbeatsound.wav")

pressed_key = ""

while pressed_key != "e" and pressed_key != "E":
    if keyboard.is_pressed("e") or keyboard.is_pressed("E"):
        pressed_key = "e"
        
        # Play the sound
        coolsound.play(-1)

        gif_path = "content/pooping.gif"

        gif_image = Image.open(gif_path)
        try:
            while True:
                current_frame = gif_image.copy()
                current_frame.show()  # Display the current frame
                gif_image.seek(gif_image.tell() + 1)  # Move to the next frame
        except EOFError:
            pass  # End of frames

        gif_image.close()

# Stop the sound and quit Pygame mixer
coolsound.stop()
pygame.mixer.quit()
