from PIL import Image


image = Image.open("test.jpg")

print(f"Currnet size of image: {image.size}")

resized_image= image.resize((500, 500))

resized_image.save("New one.jpeg")