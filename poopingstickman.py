from PIL import Image
import keyboard
import pygame

pygame.mixer.init()
coolsound = pygame.mixer.Sound("content/coolbeatsound.wav")

pressed_key = ""

while pressed_key != "e" or pressed_key != "E":
    if keyboard.is_pressed("e") or keyboard.is_pressed("E"):
        pressed_key = "e"
        
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

coolsound.stop()
pygame.mixer.quit()
