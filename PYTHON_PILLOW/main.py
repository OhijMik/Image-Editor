from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps
import time


class MyPillow:
    def __init__(self) -> None:
        self.images_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images\\"
        self.images_cropped_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_cropped\\"
        self.images_brightness_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_brightness\\"
        self.images_copied_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\two_images\\"
        self.images_filtered_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\filtered_images\\"
        self.images_black_and_white_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_black_and_white\\"
        self.images_resized_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\resized_images\\"
        self.images_reflected_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\reflected_images\\"

        
    def adjust_brightness(self, image, factor):
        opened_image = Image.open(self.images_path + image)
        adjusted = ImageEnhance.Brightness(opened_image).enhance(factor)
        adjusted.save(self.images_brightness_path + self.generate_image_name())
        adjusted.show()


    def crop_image(self, image, rect):
        opened_image = Image.open(self.images_path + image)
        cropped = opened_image.crop(rect)
        cropped.save(self.images_cropped_path + self.generate_image_name())
        cropped.show()


    def paste_image_onto_another(self, image1, image2):
        opened_image1 = Image.open(self.images_path + image1)
        opened_image2 = Image.open(self.images_path + image2)
        copyied_image = opened_image2.copy()
        copyied_image.paste(opened_image1, (0, 100))
        copyied_image.save(self.images_copied_path + self.generate_image_name())
        copyied_image.show()


    def apply_filter(self, image):
        opened_image = Image.open(self.images_path + image)
        # beach2_filtered = beach2_img.filter(ImageFilter.CONTOUR)
        # beach2_filtered = beach2_img.filter(ImageFilter.DETAIL)
        filtered = opened_image.filter(ImageFilter.SMOOTH_MORE)
        filtered.save(self.images_filtered_path + self.generate_image_name())
        filtered.show()


    def turn_images_black_and_white(self, image):
        opened_image = Image.open(self.images_path + image)
        black_and_white = opened_image.convert("L").show()
        black_and_white.save(self.images_black_and_white_path + self.generate_image_name())


    def rotate_image(self, image):
        opened_image = Image.open(self.images_path + image)
        opened_image.rotate(90).show()


    def draw_rectangle(self, image):
        opened_image = Image.open(self.images_path + image)
        copied_image = opened_image.copy()
        ImageDraw.Draw(copied_image).rectangle([(50, 10), (60, 50)], (6, 87, 90))
        copied_image.show()


    def resize_image(self, image):
        opened_image = Image.open(self.images_path + image)
        image_resized = opened_image.resize((400, 200))
        image_resized.save(self.images_resized_path + self.generate_image_name())
        image_resized.show()


    def reflect_image(self, image):
        opened_image = Image.open(self.images_path + image)
        reflected_image = ImageOps.mirror(opened_image)
        reflected_image.save(self.images_reflected_path + self.generate_image_name())
        reflected_image.show()


    def create_frame(self, image):
        opened_image = Image.open(self.images_path + image)
        image_framed = ImageOps.expand(opened_image.copy(), border=5, fill="yellow")
        image_framed.show()


    def generate_image_name(self):
        t = str(int(time.time()))
        return t + ".jpg"


    def blend_two_images(self, img1, img2):
        image1 = Image.open(self.images_path + img1)
        image2 = Image.open(self.images_path + img2)
        if image1.size == image2.size:
            new_img = Image.blend(image1, image2, 0.5)
            new_img.show()
        else:
            print("The two images don't have the same sizes")


if __name__ == "__main__":
    my_pillow = MyPillow()
    while True:
        image = input("What image do you want to edit?: ")
        print("Adjust brightness: b \nCrop image: c \nPaste image onto eachother: p \n"
            "Apply filter: f \nTurn image black and white: bw \nRotate image: rot \n"
            "Draw rectangle: d \nResize image: res \nReflect image: ref")
    
        edit = input("What do you want to edit?: ")

        match edit:
            case "b":
                brightness = float(input("What brightness do you want it to be? (default: 1.0): "))
                my_pillow.adjust_brightness(image, brightness)
            case "c":
                rect = tuple(input("What rectangle do you want to crop out? (x1, y1, x2, y2): "))
                print(rect)
                my_pillow.crop_image(image, rect)
            case "p":
                my_pillow.paste_image_onto_another(image, 0.5)
            case "f":
                my_pillow.apply_filter(image, 0.5)
            case "bw":
                my_pillow.turn_images_black_and_white(image, 0.5)
            case "rot":
                my_pillow.rotate_image(image, 0.5)
            case "d":
                my_pillow.draw_rectangle(image, 0.5)
            case "res":
                my_pillow.resize_image(image, 0.5)
            case "ref":
                my_pillow.reflect_image(image, 0.5)
            case _:
                print("Please select one of the edits from above")