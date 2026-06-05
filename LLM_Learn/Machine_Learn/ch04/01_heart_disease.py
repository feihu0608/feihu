import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. 读取数据
data = pd.read_csv("../data/heart_disease.csv")

# 2. 数据清洗
data.dropna(inplace=True)

# 3. 划分特征和标签
x = data.drop("是否患有心脏病", axis=1)
y = data["是否患有心脏病"]

# 4. 划分数据集
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
print(train_x.shape)
# 5. 特征工程
# 5.1 数值型特征: 标准化
# 5.2 类别型特征: 独热编码
numerical_features = ["年龄", "静息血压", "胆固醇", "最大心率", "运动后的ST下降", "主血管数量"]
# 类别型特征
categorical_features = ["胸痛类型", "静息心电图结果", "峰值ST段的斜率", "地中海贫血"]
# 二元特征
binary_features = ["性别", "空腹血糖", "运动性心绞痛"]

ct = ColumnTransformer([
    ("num", StandardScaler(), numerical_features),
    ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_features),
    ("binary", "passthrough", binary_features),
])

train_x = ct.fit_transform(train_x)
test_x = ct.transform(test_x)
print(train_x.shape)

# 6. 创建模型
model = LogisticRegression(
    solver="lbfgs",
    C=1.0,
    max_iter=1000000,
)

# 7. 训练模型
model.fit(train_x, train_y)

# 8. 模型评估
print(model.score(test_x, test_y))

print(model.predict(test_x[:1]), test_y[:1].values)
print(model.predict_proba(test_x[:1]))