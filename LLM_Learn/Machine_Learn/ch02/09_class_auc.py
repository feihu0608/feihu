from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

# 1. 构造数据集
x, y = make_classification(n_samples=200, n_features=20, n_classes=2, random_state=42)

# 2. 划分数据集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 3. 定义模型: 逻辑回顾
model = LogisticRegression()

# 4. 训练模型
model.fit(x_train, y_train)

# 5. 查看准确率
print(model.score(x_test, y_test))

# 6. auc值
#print(model.predict(x_test))
#print(model.predict(x_test))
#print(model.predict_proba(x_test))
print(roc_auc_score(y_test, model.predict_proba(x_test)[:, 1]))
