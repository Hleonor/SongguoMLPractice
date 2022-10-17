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
    '''
        各维数据的含义
        0：CRIM：城镇人均犯罪率
        1：ZN：住宅用地超过25,000平方英尺的比例
        2：INDUS：城镇非零售商用土地的比例
        3：CHAS：查尔斯河空变量（如果边界是河流，则为1；否则为0）
        4：NOX：一氧化氮浓度（每千万份）
        5：RM：住宅平均房间数
        6：AGE：1940年之前建成的自用单位比例
        7：DIS：到波士顿五个中心区域的加权距离
        8：RAD：辐射性公路的接近指数
        9：TAX：每1万美元的全值财产税率
        10：PTRATIO：城镇师生比例
        11：B：1000（Bk-0.63）^2，其中Bk是城镇中黑人的比例
        12：LSTAT：人口中地位低下者的比例
        13：MEDV：自住房的平均房价，以千美元计
        最后给出的是房价
    '''
    print(feature, target)  # 打印输出，可以看到数据是13维的，每一维都表示了不同的特征