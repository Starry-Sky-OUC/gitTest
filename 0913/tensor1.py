import torch
# 直接创建张量
x = torch.tensor([1.0, 2.0, 3.0])
print("x:", x)
# 复制张量
y = x.clone()
print("y:", y)
# 随机生成5*3的张量
rand_x = torch.rand(5, 3)
print("rand_x:", rand_x)