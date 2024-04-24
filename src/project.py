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

        #scan the image
        for y in range(0, heigth, self.mosaic_size):
            for x in range(0, width, self.mosaic_size):
                #Create the region to blur
                box = (x, y, x + self.mosaic_size, y + self.mosaic_size)
                box_region = self.image.crop(box)

                #(Blurred Version)
                #blurred_region = box_region.filter(ImageFilter.GaussianBlur(radius=15))
                #self.image.paste(blurred_region, box)

                #(Single Color Version)

                average_color = self.calculate_average_color(box_region)
                solid_color_image = Image.new('RGB',(self.mosaic_size, self.mosaic_size), average_color)
                self.image.paste(solid_color_image, box)


    def calculate_average_color(self, image):
        # Calculate the average color of the image
        total_average_color = tuple(int(sum(colors) / len(colors)) for colors in zip(*image.getdata()))
        return total_average_color
            
    
    def save_mosaic(self, output_name):
        if hasattr(self, 'image'):
            #convert image format to JPEG
            if self.image.mode == 'RGBA':
                self.image = self.image.convert('RGB')
            #save image in JEPG
            self.image.save(output_name, 'JPEG', quality = 95)
        else:
            print("Error: No image to save.")


def main():
    image_name = "LakeView.png"

    #sets the mosaic size  to blurr
    mosaic_size = 50

    mosaic = TurnMosaic(image_name, mosaic_size)
    mosaic.create_mosaic()

    mosaic.save_mosaic("Mosaiced_LakeView.JPEG")

    

if __name__ == "__main__":
    main()