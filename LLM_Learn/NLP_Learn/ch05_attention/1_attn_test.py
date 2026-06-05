import torch
import torch.nn as nn

# 自定义一个Attention类

class Attention(nn.Module):

    # 初始化
    def __init__(self):
        super().__init__()

    # 前向传播,传入解码器隐藏状态(N,L_dec,hidden_size),编码器输出隐藏状态(N,L_enc,hidden_size)
    def forward(self,decoder_hiddens, encoder_outputs):
        # 1. 计算注意力评分,形状(N,L_dec,L_enc)
        attn_scores = torch.bmm(decoder_hiddens, encoder_outputs.transpose(1, 2)) # transpose交换第一维和第二维,也可以写.mT转置最后两个维度

        # 2. 计算注意力权重,形状(N,L_dec,L_enc)
        attn_weights = torch.softmax(attn_scores, dim=-1)

        # 3. 加权求和,得到动态上下文向量,形状(N,L_dec,hidden_size)
        context = torch.bmm(attn_weights, encoder_outputs)

        # 4. 拼接融合向量,形状(N,L_dec,2*hidden_size)
        combined_context = torch.cat((context, decoder_hiddens), dim=-1)

        return combined_context

if __name__ == '__main__':
    attn = Attention()

    # 定义一些参数
    N = 32
    L_enc = 13
    L_dec = 15
    hidden_size = 128

    # 定义输入的隐藏状态
    encoder_outputs = torch.randn(N, L_enc, hidden_size)
    decoder_hiddens = torch.randn(N, L_dec, hidden_size)

    # 前向传播
    vectors = attn(decoder_hiddens, encoder_outputs)

    # (32,15,256)
    print(vectors.shape)
