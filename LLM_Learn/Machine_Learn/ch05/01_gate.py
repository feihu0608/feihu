# class Perceptron:
#     def __init__(self, w1, w2, theta):
#         self.w1 = w1
#         self.w2 = w2
#         self.theta = theta
#
#     def predict(self, x1, x2):
#         y = self.w1 * x1 + self.w2 * x2
#         if y <= self.theta:
#             return 0
#         else:
#             return 1
#
#     def __call__(self, x1, x2):
#         return self.predict(x1, x2)
import numpy as np

# 使用截距
class Perceptron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def predict(self, x):
        y = self.w @ x + self.b
        if y <= 0:
            return 0
        else:
            return 1

    def __call__(self, x):
        return self.predict(x)



if __name__ == '__main__':
    x1 = np.array([0,0])
    x2 = np.array([0,1])
    x3 = np.array([1,0])
    x4 = np.array([1,1])

    print("与门")
    # and_gate = Perceptron(0.5,0.5, 0.7)
    # print(and_gate(0, 0))
    # print(and_gate(0, 1))
    # print(and_gate(1, 0))
    # print(and_gate(1, 1))
    and_gate = Perceptron(np.array([0.5,0.5]),-0.7)
    print(and_gate(x1))
    print(and_gate(x2))
    print(and_gate(x3))
    print(and_gate(x4))

    print("或门")
    or_gate = Perceptron(np.array([0.5,0.5]),0)
    print(or_gate(x1))
    print(or_gate(x2))
    print(or_gate(x3))
    print(or_gate(x4))
    print("与非门")
    and_not_gate = Perceptron(np.array([-0.5,-0.5]),0.7)
    print(and_not_gate(x1))
    print(and_not_gate(x2))
    print(and_not_gate(x3))
    print(and_not_gate(x4))

    def nor_or_gate(x):
        and_not_gate = Perceptron(np.array([-0.5,-0.5]),0.7)
        or_gate = Perceptron(np.array([0.5, 0.5]), 0)
        and_gate = Perceptron(np.array([0.5, 0.5]), -0.7)
        return and_gate(np.array([and_not_gate(x), or_gate(x)]))

    print("异或门")
    print(nor_or_gate(x1))
    print(nor_or_gate(x2))
    print(nor_or_gate(x3))
    print(nor_or_gate(x4))