from PIL import Image, ImageFilter, ImageEnhance

pictures = [
    'Картинки/Ahmad.png',
    'Картинки/car.png',
    'Картинки/cat.png',
    'Картинки/collage.png',
    'Картинки/M3.png',
    'Картинки/M8.png',
    'Картинки/mem1.png',
    'Картинки/negative.jpg',
    'Картинки/resize.png',
    'Картинки/нормально.png',
    'Картинки/скала.png',
    'Картинки/скебоб.png',
    'Картинки/супермен.png',
    'Картинки/это мое.png'
]

for i in pictures:
    img = Image.open(i)
    resized_image = img.resize((100,100))
    resized_image.save(f'pic{pictures.index(i)}.png')
