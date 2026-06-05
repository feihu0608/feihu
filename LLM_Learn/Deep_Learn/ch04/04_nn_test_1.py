import torch
import torch.nn as nn


# 定义神经网络
class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # 定义层
        self.linear1 = nn.Linear(3, 4)
        self.activation1 = nn.Tanh()

        self.linear2 = nn.Linear(4, 4)
        self.activation2 = nn.ReLU()

        self.out = nn.Linear(4, 2)
        self.activation3 = nn.Softmax(dim=-1)

    def forward(self, x):
        for m in self.modules():
            if not isinstance(m, MyModule):
                x = m(x)
        return x

if __name__ == '__main__':
    # 1. 定义输入数据
    x = torch.randn(10, 3)

    # 2. 定义模型
    model = MyModule()

    y = model(x)
    print(y)

    # 查看模型的参数
    print(model.linear1.weight)
    print(model.linear1.bias)

    print("---------------------------------")
    for params in model.parameters():
        print(params)

    print("-------------------------------")
    for name, params in model.named_parameters():
        print(name)
        print(params)
    print("---------------------------")
    state_dict = model.state_dict()
    print(state_dict)

    print("------------查看模型结构: 用第三方模块-----------------")
    from torchsummary import summary
    summary(model,input_size=(3,) , batch_size=10, device='cpu')