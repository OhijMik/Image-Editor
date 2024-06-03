from PIL import Image

images_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images\\"
images_cropped_path = "C:\\Users\\jihok\\GitHub\\Image-Editor\\PYTHON_PILLOW\\images_cropped\\"

beach1Img = Image.open(images_path + "beach1.jpg")

# beach1Img.show()

beach1_cropped = beach1Img.crop((50, 0, 150, 100))
beach1_cropped.save(images_cropped_path + "beach1_cropped.jpg")
beach1_cropped.show()