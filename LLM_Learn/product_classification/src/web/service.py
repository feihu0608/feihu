"""
    服务层
"""

class TitleService:
    def __init__(self,predictor):
        self.predictor = predictor
    # 预测
    def predict(self,title):
        return self.predictor.predict(title)

