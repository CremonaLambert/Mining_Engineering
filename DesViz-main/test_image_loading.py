import pyglet

try:
    image = pyglet.resource.image('resources/backdrop_rd.jpg')
    print("Image loaded successfully!")
except Exception as e:
    print(f"Failed to load image: {e}")
