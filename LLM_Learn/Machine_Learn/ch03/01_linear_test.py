from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. 准备数据
X = [[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]]

y = [55, 65, 70, 75, 85, 50, 60, 72, 80, 58]

# 2. 定义模型:   y=ax + b
model = LinearRegression()

# 3. 训练模型
model.fit(X, y)

print(model.coef_)
print(model.intercept_)



# 画图
plt.scatter(X, y)

plt.plot(X, model.predict(X), color='red')

#plt.show()

## 验证一元解析解
import numpy as np
x = np.array(X).reshape(-1)
cov = np.cov(x, y)

b1 = cov[0, 1] / cov[0,0]
b0 = np.mean(y) - b1 * np.mean(x)
print(b0, b1)



"""
cov = np.cov(x, y)
协方差矩阵:
      x               y
x  [[ 15.21111111  43.66666667]
y  [ 43.66666667 128.66666667]]

"""