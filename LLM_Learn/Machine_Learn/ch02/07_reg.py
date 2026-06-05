import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split  # 划分数据集
from sklearn.linear_model import LinearRegression, Lasso, Ridge  # 线性回归模型, L1正则化(Lasso回归), L2正则化
from sklearn.preprocessing import PolynomialFeatures

# plt.rcParams["font.sans-serif"] = ["KaiTi"]   # windows 系统
plt.rcParams["font.sans-serif"] = ["SongTi SC"]  # macos 系统
# 不适用unicode的 -号
plt.rcParams["axes.unicode_minus"] = False

# 1. 读取数据(生成数据)  sinx
x = np.linspace(-np.pi, np.pi, 300).reshape(-1, 1)
y = np.sin(x) + np.random.normal(0, 0.3, 300).reshape(-1, 1)

# 定义画布和子图:
fig, ax = plt.subplots(2, 3, figsize=(15, 8))
ax[0, 0].scatter(x, y)
ax[0, 1].scatter(x, y)
ax[0, 2].scatter(x, y)

# 2. 数据清洗(省略)

# 3. 特征工程
## 3.1 划分数据集: 训练集和测试卷
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 4. 定义模型
model = LinearRegression()

## 过拟合
# 多项式特征
poly20 = PolynomialFeatures(degree=20)
poly20_x_train = poly20.fit_transform(x_train)
poly20_x_test = poly20.transform(x_test)
# 5. 训练模型
model.fit(poly20_x_train, y_train)  # y = w1*x1 + b

## 计算损失
train_loss = mean_squared_error(y_train, model.predict(poly20_x_train))
test_loss = mean_squared_error(y_test, model.predict(poly20_x_test))
print(model.coef_.reshape(-1), model.intercept_, train_loss, test_loss)

ax[0, 0].plot(x, model.predict(poly20.transform(x)), c='r')
ax[0, 0].text(-3, 1.5, f"训练集损失: {train_loss:.6f}")
ax[0, 0].text(-3, 1, f"测试集损失: {test_loss:.6f}")
ax[1, 0].bar(np.arange(len(model.coef_.reshape(-1))), model.coef_.reshape(-1))

print(model.score(poly20_x_test, y_test))

## L1正则化
model = Lasso(alpha=0.1)
model.fit(poly20_x_train, y_train)

train_loss = mean_squared_error(y_train, model.predict(poly20_x_train))
test_loss = mean_squared_error(y_test, model.predict(poly20_x_test))

ax[0, 1].plot(x, model.predict(poly20.transform(x)), c='r')
ax[0, 1].text(-3, 1.5, f"训练集损失: {train_loss:.6f}")
ax[0, 1].text(-3, 1, f"测试集损失: {test_loss:.6f}")
ax[1, 1].bar(np.arange(len(model.coef_.reshape(-1))), model.coef_.reshape(-1))

print(model.score(poly20_x_test, y_test))

## L2正则化
model = Ridge(alpha=0.9)
model.fit(poly20_x_train, y_train)

train_loss = mean_squared_error(y_train, model.predict(poly20_x_train))
test_loss = mean_squared_error(y_test, model.predict(poly20_x_test))

ax[0, 2].plot(x, model.predict(poly20.transform(x)), c='r')
ax[0, 2].text(-3, 1.5, f"训练集损失: {train_loss:.6f}")
ax[0, 2].text(-3, 1, f"测试集损失: {test_loss:.6f}")
ax[1, 2].bar(np.arange(len(model.coef_.reshape(-1))), model.coef_.reshape(-1))

print(model.score(poly20_x_test, y_test))

plt.show()
