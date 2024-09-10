import numpy as np
from PIL import Image
import cv2

image = Image.open("image.jpg")
image_array = np.array(image)
# 灰度操作
gray_image = image.convert("L")
gray_image_array = np.array(gray_image)

# 灰度图像直方图均衡化
equalized_gray_image_array = cv2.equalizeHist(gray_image_array)

# 彩色图像直方图均衡化（HSV）
image_hsv = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)
image_hsv[:, :, 2] = cv2.equalizeHist(image_hsv[:, :, 2])
equalized_color_image_array = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)

# 保存图像
gray_image_pil = Image.fromarray(gray_image_array)
gray_image_pil.save("gray_image.jpg")
equalized_gray_image_pil = Image.fromarray(equalized_gray_image_array)
equalized_gray_image_pil.save("equalized_gray_image.jpg")
equalized_color_image_pil = Image.fromarray(equalized_color_image_array)
equalized_color_image_pil.save("equalized_color_image.jpg")