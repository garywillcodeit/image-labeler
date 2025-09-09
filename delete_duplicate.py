import sys
import subprocess
from app.controllers.images.delete_duplicated_images_ctrl import delete_duplicated_images_ctrl

args = sys.argv
   
if __name__ == "__main__":
    if "-shutdown" in args:
        print("Shutdown requested after deletion")
    delete_duplicated_images_ctrl(logs=True)
    if "-shutdown" in args:
        command = ["shutdown", "-h", "+5"]
        subprocess.run(command)
   