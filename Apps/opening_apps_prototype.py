import subprocess

def open_folder_dialog():
    subprocess.run(["explorer", "/select,", "C:\\"])  # You can change the initial path here

if __name__ == "__main__":
    open_folder_dialog()
