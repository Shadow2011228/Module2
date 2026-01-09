from PIL import Image, ImageDraw, ImageFont

photo = Image.open('Картинки/космос.png').resize((500,500))

draw = ImageDraw.Draw(photo)

font = ImageFont.truetype("Andy MT Cyrillic Bold_0.otf", size=50)

draw.text((70, 0), "Никогда не сдавайся", fill="yellow", font=font)

font = ImageFont.truetype("Andy MT Cyrillic Bold_0.otf", size=30)

draw.text((0, 450), "Если что-то не получаеться не сдавайся", fill="yellow", font=font)

photo.show()