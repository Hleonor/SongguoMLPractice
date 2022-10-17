# import paddle.fluid as fluid
import paddle
import numpy as np
import os
import matplotlib.pyplot as plt

# 准备数据
uci_housing = paddle.text.datasets.UCIHousing(mode='train')  # 加载数据集
for i in range(10):
    feature, target = uci_housing[i]  # 返回特征和标签
    '''
        转换为tensor，tensor是paddle中的数据类型
        类似于numpy中的ndarray，作用是存储和变换数据
        tensor的作用是可以在GPU上运行，加速计算
    '''
    feature = paddle.to_tensor(feature)
    target = paddle.to_tensor(target)
    print(feature, target)