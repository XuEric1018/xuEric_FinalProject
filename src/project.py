import os
from PIL import Image
from PIL import ImageFilter
    
class TurnMosaic:
    def __init__ (self, image_name, mosaic_size):
        self.image_name = image_name
        self.mosaic_size = mosaic_size
    
    def load_image(self):
        try:
            self.image = Image.open(self.image_name)
            return True
        except FileNotFoundError:
            print(f"Error: Image '{self.image_name}' not found.")
            return False



def main():
    image_name = "LakeView.png"
    mosaic_size = 50  

if __name__ == "__main__":
    main()