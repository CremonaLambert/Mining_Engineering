from PIL import Image

# Open the image file
img = Image.open('resources/backdrop_rd.jpg')

# Save it as a PNG file
img.save('resources/backdrop_rd.png')

print("Image converted successfully!")
