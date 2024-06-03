from PIL import Image, ImageEnhance

images_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images\\"
images_cropped_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_cropped\\"
images_brightness_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_brightness\\"

beach1_img = Image.open(images_path + "beach1.jpg")

# beach1Img.show()

def adjust_brightness():
    beach2_img = Image.open(images_path + "beach2.jpg")
    beach2_adjusted = ImageEnhance.Brightness(beach1_img).enhance(0.5)
    beach2_adjusted.save(images_brightness_path + "beach2_adjusted.jpg")
    beach2_adjusted.show()


def crop_image():
    beach1_cropped = beach1_img.crop((50, 0, 150, 100))
    beach1_cropped.save(images_cropped_path + "beach1_cropped.jpg")
    beach1_cropped.show()


