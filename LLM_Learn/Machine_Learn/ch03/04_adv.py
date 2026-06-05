import pandas as pd
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. 读取数据
data = pd.read_csv("../data/advertising.csv")

# 2. 数据清洗
data.drop(data.columns[0], axis=1, inplace=True)
data.dropna(inplace=True)

# 3. 提前特征和标签
x = data.drop("Sales", axis=1)
y = data["Sales"]

# 4. 划分数据集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 5. 对特征做标准化
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# 6. 选择模型
model_1 = LinearRegression()
model_2 = SGDRegressor()

# 7. 训练模型
model_1.fit(x_train, y_train)
model_2.fit(x_train, y_train)

# 8. 查看参数
print(model_1.coef_, model_1.intercept_)
print(model_2.coef_, model_2.intercept_)

# 9. R^2决定系数
print(model_1.score(x_test, y_test))
print(model_2.score(x_test, y_test))

print("-======")
print(model_1.predict(x_test[0:3]), y_test[0:3].values)
print(model_2.predict(x_test[0:3]), y_test[0:3].values)