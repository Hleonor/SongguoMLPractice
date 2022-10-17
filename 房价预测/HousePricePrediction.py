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

# 切分数据集
train_dataset = paddle.text.datasets.UCIHousing(mode='train')  # 训练集
eval_dataset = paddle.text.datasets.UCIHousing(mode='test')  # 测试集
train_loader = paddle.io.DataLoader(train_dataset, batch_size=32, shuffle=True)  # 训练集加载器，每次加载32个数据
eval_loader = paddle.io.DataLoader(eval_dataset, batch_size=8, shuffle=False)  # 测试集加载器，每次加载8个数据，测试不打乱顺序

# 网络搭建
class MyDNN(paddle.nn.Layer):  # 继承paddle.nn.Layer类
    def __int__(self):
        super(MyDNN, self).__init__()  # 调用父类的构造函数
        self.linear = paddle.nn.layer(13, 1, None)  # 线性层，输入13维，输出1维，None表示不使用激活函数
    def forward(self, *inputs):  # 定义前向传播
        x = self.linear(inputs)
        return x

# 模型训练
model = MyDNN()  # 实例化模型
model.train() # 训练模式
mse_loss = paddle.nn.MSELoss()  # 均方误差损失函数
opt=paddle.optimizer.SGD(learning_rate=0.00005, parameters=model.parameters())  # 优化器，使用随机梯度下降，学习率为0.01，优化模型参数
epochs_nums = 200  # 训练轮数

for epochs in range(epochs_nums):  # 训练轮数
    for batch_id, data in enumerate(train_loader):  # 遍历训练集
        feature = data[0]  # 获取特征
        label = data[1]  # 获取标签
        print(feature, label)  # 打印输出，可以看到数据是13维的，每一维都表示了不同的特征

















