from PIL import Image
# 打开图片
image = Image.open("image.jpg")
# 处理前
image.show()
# 缩放
new_size = (800, 600)  # 新的尺寸
resized_image = image.resize(new_size)
# 旋转
angle = 45  # 旋转角度
rotated_image = resized_image.rotate(angle)
# 转换为RGB模式
rgb_image = rotated_image.convert("RGB")
# 处理后
rgb_image.show()
# 保存处理后的图片
rgb_image.save("image2.jpg", format="JPEG")