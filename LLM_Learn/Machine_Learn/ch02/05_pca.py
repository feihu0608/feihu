import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

n = 1000
# 1. 构造特征
## 1.1 生成主成分1 2
pc1 = np.random.normal(0, 1, n)
pc2 = np.random.normal(0, 0.5, n)
## 1.2 构造特征
f1 = pc1 + pc2
f2 = pc1 - pc2
f3 = pc1 + np.random.normal(0, 0.1, n)

## 1.3 特征向量
x = np.vstack((f1, f2, f3)).T
print(x.shape)

# 2. 主成分分析  n_components: 如果是整数,表示要保留的维度 如果是浮点数: 表示保留的信息量
pca =PCA(n_components=0.88)

x_pca = pca.fit_transform(x)
print(x_pca.shape)

# 画图
fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(x[:, 0], x[:, 1], x[:, 2], c='g')
ax1.set_title("Before PCA")
ax1.set_xlabel("F1")
ax1.set_ylabel("F2")
ax1.set_zlabel("F3")

ax2= fig.add_subplot(122)
ax2.scatter(x_pca[:, 0], x_pca[:, 1], c='g')
ax2.set_title("After PCA")
ax2.set_xlabel("F1")
ax1.set_ylabel("F2")

plt.show()