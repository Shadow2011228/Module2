from PIL import Image, ImageFilter, ImageEnhance


img = Image.open('Картинки/car.png')

print("Размер:", img.size)
print("Формат:", img.format)
print("Режим цвета:", img.mode)

img.show()

# Уменьшаем изображение в 2 раза
resized_image = img.resize((img.size[0] // 2, img.size[1] // 2))
# resized_image.show()

# Обрезаем изображение до квадрата с мордочкой
cropped_image = img.crop((200, 100, 500, 400))
# cropped_image.show()

# Применяем размытие
blurred_image = img.filter(ImageFilter.BLUR)
blurred_image = blurred_image.filter(ImageFilter.BLUR)
blurred_image = blurred_image.filter(ImageFilter.BLUR)
blurred_image = blurred_image.filter(ImageFilter.BLUR)
# blurred_image.show()

# Применяем размытие по Гауссу
blurred_image = img.filter(ImageFilter.GaussianBlur(radius=50))
# blurred_image.show()

# Изменяем яркость (1.0 - оригинал, меньше 1 - темнее, больше 1 - светлее)
enhancer = ImageEnhance.Brightness(img)
brighter_image = enhancer.enhance(0.5)
# brighter_image.show()

# Изменяем контрастность (аналогично яркости)
contrast_enhancer = ImageEnhance.Contrast(img)
high_contrast_image = contrast_enhancer.enhance(2.5)
# high_contrast_image.show()

# Изменяем контрастность (аналогично яркости)
contrast_enhancer = ImageEnhance.Contrast(img)
negative_image = contrast_enhancer.enhance(-1)

# Сохраняем изображение
negative_image.save('negative.jpg')
