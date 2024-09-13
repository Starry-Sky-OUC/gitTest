import torch

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
# 加
add = a + b
print("加:", add)
# 减
sub = a - b
print("减:", sub)
# 乘
mul = a * b
print("乘:", mul)
# 除
div = a / b
print("除:", div)
# 矩阵乘
mat1 = torch.tensor([[1, 2], [3, 4]])
mat2 = torch.tensor([[5, 6], [7, 8]])
matmul = torch.matmul(mat1, mat2)
print("mat1 * mat2:\n", matmul)
# 求和
sum = torch.sum(a)
print("求和:", sum)
# 均值
mean = torch.mean(a)
print("均值:", mean)
# 最大值
max = torch.max(a)
print("最大值:", max)
# 最小值
min = torch.min(a)
print("最小值:", min)