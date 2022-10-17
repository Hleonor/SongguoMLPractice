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
    # print(feature, target)  # 打印输出，可以看到数据是13维的，每一维都表示了不同的特征

# 切分数据集
train_dataset = paddle.text.datasets.UCIHousing(mode='train')  # 训练集
eval_dataset = paddle.text.datasets.UCIHousing(mode='test')  # 测试集
train_loader = paddle.io.DataLoader(train_dataset, batch_size=32, shuffle=True)  # 训练集加载器，每次加载32个数据
eval_loader = paddle.io.DataLoader(eval_dataset, batch_size=8, shuffle=False)  # 测试集加载器，每次加载8个数据，测试不打乱顺序


# 网络搭建
# 定义全连接网络
class MyDNN(paddle.nn.Layer):  # 继承paddle.nn.Layer类
    def __init__(self):
        super(MyDNN, self).__init__()  # 调用父类的构造函数
        # 定义一层全连接层，输入维度是13，输出维度是1，激活函数为None，即不使用激活函数
        self.linear = paddle.nn.Linear(13, 1, None)

    # 网络的前向计算函数
    def forward(self, inputs):
        x = self.linear(inputs)
        return x


Batch = 0
Batchs = []
all_train_accs = []


def draw_train_acc(Batchs, train_accs):
    title = "training accs"
    plt.title(title, fontsize=24)
    plt.xlabel("batch", fontsize=14)
    plt.ylabel("acc", fontsize=14)
    plt.plot(Batchs, train_accs, color='green', label='training accs')
    plt.legend()
    plt.grid()
    plt.show()


all_train_loss = []


def draw_train_loss(Batchs, train_loss):
    title = "training loss"
    plt.title(title, fontsize=24)
    plt.xlabel("batch", fontsize=14)
    plt.ylabel("loss", fontsize=14)
    plt.plot(Batchs, train_loss, color='red', label='training loss')
    plt.legend()
    plt.grid()
    plt.show()


# 模型训练
model = MyDNN()  # 模型实例化
model.train()  # 训练模式
mse_loss = paddle.nn.MSELoss()  # 均方误差损失函数
opt = paddle.optimizer.SGD(learning_rate=0.0005, parameters=model.parameters())  # 优化器，使用随机梯度下降，学习率为0.01，优化模型参数
epochs_num = 200  # 迭代次数

for pass_num in range(epochs_num):  # 训练轮数
    for batch_id, data in enumerate(train_loader()):  # 遍历训练集
        feature = data[0]  # 获取特征
        label = data[1]  # 获取标签，即房价
        predict = model(feature)  # 数据传入model，前向传播，得到预测值
        loss = mse_loss(predict, label)  # 计算损失

        if batch_id != 0 and batch_id % 10 == 0:
            Batch = Batch + 20
            Batchs.append(Batch)
            all_train_loss.append(loss.numpy()[0])
            print("epoch: {}, step: {}, train_loss: {}".format(pass_num, batch_id, loss.numpy()[0]))  # 将tensor转换为numpy，再转换为python的标量
        loss.backward()  # 反向传播，计算梯度
        opt.step()  # 优化器更新参数
        opt.clear_grad()  # opt.clear_grad()来重置梯度
paddle.save(model.state_dict(), 'MyDNN')  # 保存模型
draw_train_loss(Batchs, all_train_loss)  # 绘制训练集的损失曲线
