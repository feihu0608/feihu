import numpy as np

x = np.array([[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]])

x = np.hstack((np.ones((10, 1)), x))
print(x)
y = np.array([[55], [65], [70], [75], [85], [50], [60], [72], [80], [58]])  # 因变量，数学考试成绩

n = x.shape[0]


# 定义目标函数(损失函数)   b0 + b1*x   ( [b0, b1] * [1, x] - y) ** 2
def loss_fn(beta):
    return (x @ beta - y).T @ (x @ beta - y) / n


def grad_fn(beta):
    return x.T @ (x @ beta - y) / n * 2


beta = np.array([[1], [1]])
lr = 0.01
iter = 4000
beta0 = []
beta1 = []
for i in range(iter):
    beta0.append(beta[0][0])
    beta1.append(beta[1][0])
    # 更新参数
    beta = beta - lr * grad_fn(beta)

    print(f"第{i + 1}次迭代: {beta}")

import matplotlib.pyplot as plt

plt.plot(beta0, beta1)
plt.show()
