import torch

x = torch.tensor([2.0, 3.0], requires_grad=True)
# 定义函数
y = x[0]**2 + x[1]**3
print("y:", y)
# 计算梯度
y.backward()
print("grad:", x.grad)