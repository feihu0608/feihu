import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split  # 划分数据集
from sklearn.linear_model import LinearRegression  # 线性回归模型
from sklearn.preprocessing import PolynomialFeatures

#plt.rcParams["font.sans-serif"] = ["KaiTi"]   # windows 系统
plt.rcParams["font.sans-serif"] = ["SongTi SC"]  # macos 系统
# 不适用unicode的 -号
plt.rcParams["axes.unicode_minus"] = False


# 1. 读取数据(生成数据)  sinx
x = np.linspace(-np.pi, np.pi, 300).reshape(-1, 1)
y = np.sin(x) + np.random.normal(0, 0.3, 300).reshape(-1, 1)

# 定义画布和子图:
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
ax[0].scatter(x, y)
ax[1].scatter(x, y)
ax[2].scatter(x, y)

# 2. 数据清洗(省略)

# 3. 特征工程
## 3.1 划分数据集: 训练集和测试卷
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 4. 定义模型
model = LinearRegression()

## 欠拟合
# 5. 训练模型
model.fit(x_train, y_train)  # y = w1*x1 + b

## 计算损失
train_loss = mean_squared_error(y_train, model.predict(x_train))
test_loss = mean_squared_error(y_test, model.predict(x_test))
print(model.coef_, model.intercept_, train_loss, test_loss)

# 6. 画图
ax[0].plot(x, model.predict(x), c='r')
ax[0].text(-3, 1.5, f"训练集损失: {train_loss:.6f}")
ax[0].text(-3, 1,   f"测试集损失: {test_loss:.6f}")

## 恰好拟合
# 多项式特征
poly5 = PolynomialFeatures(degree=5)
poly5_x_train = poly5.fit_transform(x_train)
poly5_x_test = poly5.transform(x_test)
# 5. 训练模型
model.fit(poly5_x_train, y_train)  # y = w1*x1 + b

## 计算损失
train_loss = mean_squared_error(y_train, model.predict(poly5_x_train))
test_loss = mean_squared_error(y_test, model.predict(poly5_x_test))
print(model.coef_, model.intercept_, train_loss, test_loss)


ax[1].plot(x, model.predict(poly5.transform(x)), c='r')
ax[1].text(-3, 1.5, f"训练集损失: {train_loss:.6f}")
ax[1].text(-3, 1,   f"测试集损失: {test_loss:.6f}")


## 恰好拟合
# 多项式特征
poly20 = PolynomialFeatures(degree=20)
poly20_x_train = poly20.fit_transform(x_train)
poly20_x_test = poly20.transform(x_test)
# 5. 训练模型
model.fit(poly20_x_train, y_train)  # y = w1*x1 + b

## 计算损失
train_loss = mean_squared_error(y_train, model.predict(poly20_x_train))
test_loss = mean_squared_error(y_test, model.predict(poly20_x_test))
print(model.coef_, model.intercept_, train_loss, test_loss)


ax[2].plot(x, model.predict(poly20.transform(x)), c='r')
ax[2].text(-3, 1.5, f"训练集损失: {train_loss:.6f}")
ax[2].text(-3, 1,   f"测试集损失: {test_loss:.6f}")

plt.show()