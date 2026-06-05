import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import MinMaxScaler, StandardScaler

x = np.array([[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]])

y = np.array([[55], [65], [70], [75], [85], [50], [60], [72], [80], [58]]).reshape(-1)  # 因变量，数学考试成绩

sgd = SGDRegressor(
    loss="squared_error",
    penalty="l2",
    alpha=0.0000001,
    learning_rate="constant",  # 学习率策略
    eta0=0.0001,  # 学习率
    max_iter=200000000,
    tol=1e-30,  # 当梯度小于这个值时会提前停止
    early_stopping=False,
)



sgd.fit(x, y)

print(sgd.coef_)
print(sgd.intercept_)