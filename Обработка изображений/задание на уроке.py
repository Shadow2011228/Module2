from PIL import Image, ImageDraw, ImageFont


photo = Image.open('cat.png').resize((500,500))

draw = ImageDraw.Draw(photo)

font = ImageFont.truetype("Norse-Bold.ttf", size=30)

draw.text((50, 400), "I\n am programmist", fill="black", font=font)
photo.show()

