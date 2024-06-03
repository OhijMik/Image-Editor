from PIL import Image, ImageEnhance, ImageFilter

images_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images\\"
images_cropped_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_cropped\\"
images_brightness_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_brightness\\"
images_copied_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\two_images\\"
images_filtered_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\filtered_images\\"

beach1_img = Image.open(images_path + "beach1.jpg")

# beach1Img.show()

def adjust_brightness():
    beach2_img = Image.open(images_path + "beach2.jpg")
    beach2_adjusted = ImageEnhance.Brightness(beach2_img).enhance(0.5)
    beach2_adjusted.save(images_brightness_path + "beach2_adjusted.jpg")
    beach2_adjusted.show()


def crop_image():
    beach1_cropped = beach1_img.crop((50, 0, 150, 100))
    beach1_cropped.save(images_cropped_path + "beach1_cropped.jpg")
    beach1_cropped.show()


def paste_image_onto_another():
    beach1_img = Image.open(images_path + "beach1.jpg")
    beach2_img = Image.open(images_path + "beach2.jpg")
    beach2_copy = beach2_img.copy()
    beach2_copy.paste(beach1_img, (0, 100))
    beach2_copy.save(images_copied_path + "beach2_copy.jpg")
    beach2_copy.show()


def apply_filter():
    beach2_img = Image.open(images_path + "beach2.jpg")
    # beach2_filtered = beach2_img.filter(ImageFilter.CONTOUR)
    # beach2_filtered = beach2_img.filter(ImageFilter.DETAIL)
    beach2_filtered = beach2_img.filter(ImageFilter.SMOOTH_MORE)
    beach2_filtered.save(images_filtered_path + "beach2_filtered.jpg")
    beach2_filtered.show()

apply_filter()