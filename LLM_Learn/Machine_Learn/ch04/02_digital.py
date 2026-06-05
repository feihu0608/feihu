import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
# 1.读取数据
data = pd.read_csv("../data/train.csv")
# plt.imshow(data.iloc[4, 1:].values.reshape(28,28), cmap='Grays_r')
# plt.show()
# 2. 划分特征和标签
x = data.iloc[:, 1:]
y = data.iloc[:, 0]

# 3. 划分数据集合
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.2, random_state = 42)

# 4. 对特征做归一化
scaler = MinMaxScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.transform(test_x)

# 5. 选择模型
model = LogisticRegression(
    max_iter = 10000,
)

# 6. 训练模型
model.fit(train_x, train_y)

# 7. 模型评估
print(model.score(test_x, test_y))

print(model.predict(test_x[20:21]), test_y[20:21].values)

plt.imshow(test_x[20:21].reshape(28,28), cmap='Grays_r')
plt.show()
