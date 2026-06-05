import torch
import torch.nn as nn

# 定义神经网络
class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # 定义层
        self.linear1 = nn.Linear(3, 4)
        self.linear2 = nn.Linear(4, 4)
        self.out = nn.Linear(4, 2)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.tanh(x)

        x = self.linear2(x)
        x = torch.relu(x)

        x = self.out(x)
        return torch.softmax(x, dim=-1)

if __name__ == '__main__':
    # 1. 定义输入数据
    x = torch.randn(10, 3)

    # 2. 定义模型
    model = MyModule()

    # 3. 前向传播
    y = model(x)

    nn.Sigmoid
    print(y)




