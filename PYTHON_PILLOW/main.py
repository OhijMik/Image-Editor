from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps
import time
import pygame


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
        brightness = float(input("What brightness do you want it to be? (default: 1.0): "))
        opened_image = Image.open(self.images_path + image)
        adjusted = ImageEnhance.Brightness(opened_image).enhance(brightness)
        adjusted.save(self.images_brightness_path + self.generate_image_name())
        adjusted.show()

    def crop_image(self, image):
        rect = str_to_tup(input("What is the rectangle coordinates of the crop? (x1, y1, x2, y2): "))
        opened_image = Image.open(self.images_path + image)
        cropped = opened_image.crop(rect)
        cropped.save(self.images_cropped_path + self.generate_image_name())
        cropped.show()

    def paste_image_onto_another(self, image1):
        image2 = input("Select another image to paste: ")
        coordinate = str_to_tup(input("What coordinate do you want to paste the image?: "))
        opened_image1 = Image.open(self.images_path + image1)
        opened_image2 = Image.open(self.images_path + image2)
        copyied_image = opened_image2.copy()
        copyied_image.paste(opened_image1, coordinate)
        copyied_image.save(self.images_copied_path + self.generate_image_name())
        copyied_image.show()

    def apply_filter(self, image):
        opened_image = Image.open(self.images_path + image)
        while True:
            filter = input("Which filter do you want? (contour, detail, smooth_more): ")
            if filter == "contour":
                filtered = opened_image.filter(ImageFilter.CONTOUR)
                break
            elif filter == "detail":
                filtered = opened_image.filter(ImageFilter.DETAIL)
                break
            elif filter == "smooth_more":
                filtered = opened_image.filter(ImageFilter.SMOOTH_MORE)
                break
            else:
                print("Please enter a valid option. \n")
        filtered.save(self.images_filtered_path + self.generate_image_name())
        filtered.show()

    def turn_images_black_and_white(self, image):
        opened_image = Image.open(self.images_path + image)
        black_and_white = opened_image.convert("L")
        black_and_white.show()
        black_and_white.save(self.images_black_and_white_path + self.generate_image_name())

    def rotate_image(self, image):
        opened_image = Image.open(self.images_path + image)
        degree = int(input("Enter how many degree you want to rotate the image by: "))
        opened_image.rotate(degree).show()

    def draw_rectangle(self, image):
        opened_image = Image.open(self.images_path + image)
        copied_image = opened_image.copy()
        ImageDraw.Draw(copied_image).rectangle([(50, 10), (60, 50)], (6, 87, 90))
        copied_image.show()

    def resize_image(self, image):
        opened_image = Image.open(self.images_path + image)
        w = int(input("Enter the desired width: "))
        h = int(input("Enter the desired height: "))
        image_resized = opened_image.resize((w, h))
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


def str_to_tup(s):
    lst = []
    temp = ""
    for i in s:
        if i.isnumeric():
            temp += i
        else:
            if temp != "":
                lst.append(int(temp))
                temp = ""
    if temp != "":
        lst.append(int(temp))
        temp = ""
    return tuple(lst)


if __name__ == "__main__":
    my_pillow = MyPillow()
    while True:
        image = input("What image do you want to edit?: ")
        print("Adjust brightness: b \nCrop image: c \nPaste image onto eachother: p \n"
            "Apply filter: f \nTurn image black and white: bw \nRotate image: rot \n"
            "Resize image: res \nReflect image: ref")

        edit = input("Which function do you want to apply to your image?: ")

        match edit:
            case "b":
                my_pillow.adjust_brightness(image)
            case "c":
                my_pillow.crop_image(image)
            case "p":
                my_pillow.paste_image_onto_another(image)
            case "f":
                my_pillow.apply_filter(image)
            case "bw":
                my_pillow.turn_images_black_and_white(image)
            case "rot":
                my_pillow.rotate_image(image)
            case "res":
                my_pillow.resize_image(image)
            case "ref":
                my_pillow.reflect_image(image)
            case _:
                print("Please select one of the edits from above")
        break
