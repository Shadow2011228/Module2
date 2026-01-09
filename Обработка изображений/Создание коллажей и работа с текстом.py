from PIL import Image

collage = Image.new('RGB', (800,600), color='purple')


img = Image.open('Картинки/car.png').resize((300,200))
collage.paste(img, (250,200))

img = Image.open('Картинки/M3.png').resize((300,200))
collage.paste(img, (0,0))

img = Image.open('Картинки/M8.png').resize((300,200))
collage.paste(img, (500,0))

collage.show()

collage.save('collage.png')