import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, sobel

image = Image.open("image.jpg")
image_array = np.array(image)

# 图像模糊（高斯滤波）
blurred_image_array = gaussian_filter(image_array, sigma=2)

if image.mode == 'RGBA':
    blurred_image_array = blurred_image_array[:, :, :3]

# 灰度转换
gray_image_array = np.array(Image.open("image.jpg").convert("L"))

# 图像导数（Sobel算子）
sobel_x = sobel(gray_image_array, axis=0)
sobel_y = sobel(gray_image_array, axis=1)
sobel_image_array = np.hypot(sobel_x, sobel_y)

# 保存处理后的图像
blurred_image_pil = Image.fromarray(blurred_image_array.astype(np.uint8))
blurred_image_pil.save("blurred_image.jpg")
sobel_image_pil = Image.fromarray(sobel_image_array.astype(np.uint8))
sobel_image_pil.save("sobel_image.jpg")