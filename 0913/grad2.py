import torch

x = torch.tensor([2.0, 3.0], requires_grad=True)
# 定义函数
y = x + 1
print("y:", y)
z = y * y * 3
print("z:", z)
out = z.mean()
print("out:", out)
# 计算梯度
out.backward()
print("grad:", x.grad)