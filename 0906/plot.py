from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("image.jpg")
# 转换为灰度图
gray_image = image.convert("L")
# 获取图像像素数据
pixels = list(gray_image.getdata())
width, height = gray_image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

# 图像轮廓
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Image Contour")
plt.contour(pixels, cmap='gray')
plt.axis('off')

# 图像直方图
plt.subplot(1, 2, 2)
plt.title("Histogram")
plt.hist(gray_image.histogram(), bins=256, range=[0, 256], color='black', alpha=0.75)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# 保存图像
plt.savefig("plt.png")
# 显示图像
plt.show()