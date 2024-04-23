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
        
    def create_mosaic(self):
        #Solves: AttributeError: 'TurnMosaic' object has no attribute 'image'
        if not hasattr(self, 'image'):
            if not self.load_image():
                return

        width, heigth = self.image.size
        for y in range(0, heigth, self.mosaic_size):
            for x in range(0, width, self.mosaic_size):
                #Create the region to blur
                box = (x, y, x + self.mosaic_size, y + self.mosaic_size)

                box_region = self.image.crop(box)

                blurred_region = box_region.filter(ImageFilter.GaussianBlur(radius=15))

                self.image.paste(blurred_region, box)
    
    def save_mosaic(self, output_name):
        if hasattr(self, 'image'):
            self.image.save(output_name)
        else:
            print("Error: No image to save.")


def main():
    image_name = "LakeView.png"
    mosaic_size = 50  

    mosaic = TurnMosaic(image_name, mosaic_size)
    mosaic.create_mosaic()

    mosaic.save_mosaic("Mosaiced_LakeView.png")

    

if __name__ == "__main__":
    main()