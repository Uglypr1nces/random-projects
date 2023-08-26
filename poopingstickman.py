from PIL import Image
import keyboard

from pydub import AudioSegment
from pydub.playback import play



pressed_key = ""
while pressed_key != "e" or "E":
    if keyboard.is_pressed("e") or keyboard.is_pressed("E"):
        pressed_key = "e"
        
        song = AudioSegment.from_wav("content/coolbeatsound.wav")
        play(song)

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
