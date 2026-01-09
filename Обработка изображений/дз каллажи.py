from PIL import Image

collage = Image.new('RGB', (800,600), color='purple')

img = Image.open('Картинки/mem1.png').resize((200,200))
collage.paste(img, (0,0))

img = Image.open('Картинки/супермен.png').resize((200,200))
collage.paste(img, (0,200))

img = Image.open('Картинки/это мое.png').resize((200,200))
collage.paste(img, (0,400))

img = Image.open('Картинки/скебоб.png').resize((200,200))
collage.paste(img, (200,0))

img = Image.open('Картинки/скала.png').resize((200,200))
collage.paste(img, (200,200))

img = Image.open('Картинки/нормально.png').resize((200,200))
collage.paste(img, (200,400))

collage.show()