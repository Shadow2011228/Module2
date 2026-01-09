from PIL import Image, ImageDraw, ImageFont


photo = Image.open('Картинки/mem1.png').resize((500,500))

draw = ImageDraw.Draw(photo)

font = ImageFont.truetype("FontsBombILoveGrapes.ttf", size=30)

# font = ImageFont.load_default()

draw.text((50, 400), "O, Holero\n it's Freddy Fasberg", fill="yellow", font=font)
photo.show()

