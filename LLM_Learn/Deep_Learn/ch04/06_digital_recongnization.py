import torch
import torch.nn as nn

from common.load_data import load_digtial_data

# 1. 读取数据
x_train, x_test, y_train, y_test = load_digtial_data()

# 2. 定义模型
model = nn.Sequential(
    nn.Linear(784, 50),
    nn.ReLU(),

    nn.Linear(50, 100),
    nn.ReLU(),

    nn.Linear(100, 10)
    # nn.Softmax(dim=-1)  # 定义模型是, Softmax省略, 因为Softmax和损失函数已经绑在一起
)

# 3. 加载状态字典
state_dict = torch.load('../data/nn_example.pt', map_location="cpu")
model.load_state_dict(state_dict)

# 5. 预测
y_pred = model(x_train)


# 6. 计算准确率
## 6.1 分子: 预测的对的个数
y_class = torch.argmax(y_pred, dim=-1)
# print((y_class == y_test).sum().item())
# print(torch.sum(y_class == y_test).item()   )
# print(torch.sum(y_class.eq(y_test)).item()   )

acc_cnt = torch.sum(y_class == y_train).item()

## 6.2 分母: 参与预测的数量
total_cnt = len(y_train)

acc = acc_cnt / total_cnt

print(acc)














