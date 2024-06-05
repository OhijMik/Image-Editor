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

        
    def adjust_brightness(self, image):
        opened_image = Image.open(self.images_path + image)
        adjusted = ImageEnhance.Brightness(opened_image).enhance(0.5)
        adjusted.save(self.images_brightness_path + self.generate_image_name())
        adjusted.show()


    def crop_image(self, image):
        opened_image = Image.open(self.images_path + image)
        cropped = opened_image.crop((50, 0, 150, 100))
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


my_pillow = MyPillow()

image = input("What image do you want to edit?: ")