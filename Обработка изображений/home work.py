from PIL import Image, ImageFilter, ImageEnhance

img = Image.open('Картинки/Ahmad.png')

print("Размер:", img.size)
print("Формат:", img.format)
print("Режим цвета:", img.mode)

img.show()

resized_image = img.resize((img.size[0] - 120, img.size[1] - 120))
resized_image.show()

blurred_image = img.filter(ImageFilter.GaussianBlur(radius=50))
# blurred_image.show()

contrast_enhancer = ImageEnhance.Contrast(img)
high_contrast_image = contrast_enhancer.enhance(2.5)
# high_contrast_image.show()

resized_image.save('resize.png')
