# encoding: utf-8
"""
 @project:ML_Algorithms
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 3/1/19 9:21 AM
 @desc: 朴素贝叶斯算法总结
"""

"""
 1.站在后验概率的角度，机器学习所要实现的是基于有限的训练样本集尽可能准确地估计出后验概率P(C|X),X是训练样本各个特征值组合成的向量；
   大体来说，要得到P(C|X)的值，有两种实现策略
      (1)判别式模型(discriminative models)
         给定X，通过 直接建模 P(C|X)来预测C，这种类型的模型有决策树、BP神经网络、SVM、逻辑斯蒂回归等
      (2)生成式模型(generative models)
         给定X，先对联合概率分布P(X,C)建模，然后由此再获得P(C|X)，这种类型的模型有朴素贝叶斯、高斯判别分析等
            
 2.在前面的学习中，我们知道基于贝叶斯定理，P(C|X)可以写成：
               P(C|X) = P(X|C)*P(C)/P(X),
   而起到判别作用的主要是P(X|C)和P(C)，P(C)是类的先验概率，P(X|C)是样本X相对于类标签C的条件概率，或称为似然(likelihood);
 *【重点】  
      根据大数定律，当训练集包含充足的独立同分布样本时，P(C)可通过各类样本出现的频率来进行估计;
      而对于P(X|C)，根据不同的学派，有着不同的求法.
      
      (1)极大似然估计（MLE，由频率学派提出）
         假设各个样本是独立同分布的，从数据集入手，找出一组参数集θ，使得数据集D中每个样本的特征值与参数集线性组合之后，结果尽可能地和标签接近
         举个抛硬币的例子，抛了10次，正面朝上的次数为8次，问你下一次抛硬币时，正面朝上的概率是多少？ 显然推测是80%，似然估计就是这样子的思想,
         一种结果导向的求法，由客观的事实，来推测参数，以拟合事实，这也符合频率学派的思想。（假设很重要，强调样本独立同分布，否则误差会很大）
         
      (2)朴素贝叶斯决策(NB,由贝叶斯学派提出)
         朴素贝叶斯分类器采用了“特征之间相互独立”假设，即认为特征之间相关性很低，因此可以将P(X|C)简化为
                P(X|C) = P(x0|C)P(x1|C)P(x2|C)...P(xn|C)
         那么如何求解P(xi|C=ci)呢？
                P(xi|C=ci) = P(xi,C=ci) / P(C=ci)
            (a)如果是离散属性的话，P(xi,C=ci)可以用样本中特征值为xi且类别为ci的样本个数n_xi_ci代替，P(C=ci)可以用类别为ci的样本数n_ci
            代替，即用频率来近似概率，在实际中，为了防止出现0概率异常，在此基础上，可以使用拉普拉斯平滑方法；
            
            (b)如果是连续属性的话，考虑概率密度函数，假设p(xi|C=ci)符合正态分布，然后进行求解；
               举个栗子，西瓜分为好瓜和坏瓜两种类别，有一个属性是含糖率，为连续属性，在训练集中，我们取出所有类别为好瓜的样本的含糖率数值，
            计算出它的均值和标准差，作为正态分布函数的参数，从而求出如p(含糖率=0.37|好瓜)的值了，同理也可以得到p(含糖率=0.37|坏瓜)的值。
                
        【这一部分的内容，详细参看《机器学习》周志华，P150 7.3节，有具体案例】         
         
 3.朴素贝叶斯算法优点:
    (1)对小规模的数据表现很好，能够处理多分类任务，适合增量式训练
    (2)对缺失数据不太敏感，算法也比较简单，在文本分类任务中表现很好
    
 4.朴素贝叶斯算法缺点:
    (1)朴素贝叶斯算法的假设是样本各个属性之间相互独立，但是在实际应用中往往不成立，这个问题，后来通过半朴素贝叶斯分类算法得到改善
    
    (2)需要知道先验概率，而先验概率取决于假设，而常见的假设高斯分布、多项式分布、伯努利分布，可能会因为假设的原因导致预测效果不佳
        (a)高斯分布，即假设特征的先验概率服从正态分布，如下式：
            P(X=Xi|C=Cj) = 1/(np.sqrt(2π)*ρ) * np.exp(-(xi-μ)^2 / 2ρ^2)
           其中，P(X=Xmi|C=Cj)表示第j类样本中第i个属性取值为Xi的概率，ρ为第j类样本中第i个属性值的标准差，μ为均值
            
        (b)多项式分布,即假设特征的先验概率为多项式分布，如下式：
            P(X=Xi|C=Cj) = num_xi_cj / num_cj，其实就是 第j类样本的第i个特征取值为Xi的样本数 / 第j类样本的总数，一种频率的计算方式
           然而，实际中可能出现某类样本中某特征值的样本数为零的情况，引入拉普拉斯平滑来解决，多项式分布的式子最终为：
            P(X=Xi|C=Cj) = (num_xi_cj+alpha) / (num_cj + n*alpha) , alpha为一个大于0的常数，常取1，n为第i个特征的特征值个数
            
        (c)伯努利分布，即假设特征的先验概率为二元伯努利分布，如下式：
            P(X=Xi|C=Cj) = P(Xi|C=Cj)*Xi_test + (1-P(Xi|C=Cj))*(1-Xi_test) , Xi_test取0或1
            伯努利模型中，每个特征的取值都是布尔型的，要么是0，要么是1，比如说，特征A的取值有[1,2,3],如果测试样本中，特征A的值为1或2或3，
            那么把测试样本中特征A的值改为1，如果测试样本中特征A的取值为4，不在训练集的范围内，那么把测试样本中特征A的取值改为0
            
            
    (3)由于我们是通过先验概率P(C)和似然(P(X|C))来计算后验概率从而决定分类，所以分类决策存在一定的错误率
    
    (4)数据的表现形式是连续特征、离散特征还是二元特征都会对模型的概率计算结果产生很大的影响
"""
