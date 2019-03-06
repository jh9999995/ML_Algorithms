# encoding: utf-8
"""
 @project:ML_Algorithms
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 3/6/19 4:15 PM
 @desc: 逻辑回归算法总结
"""

"""
 前面的学习，我们主要了解了如何从线性回归到逻辑回归，逻辑回归的损失函数的由来，损失函数的最优化求解这三个方面
   
 在总结部分，我想补充三点，二元逻辑回归的正则化，二元逻辑回归推广到多分类，二元逻辑回归的优缺点
    
 1.二元逻辑回归的正则化
    逻辑回归也面临着过拟合的问题，所以我们也要考虑正则化，加一个调节因子，常见的有L1正则化和L2正则化
    (1)L1正则化
       相比普通的逻辑回归损失函数，增加了L1的范数做作为惩罚，超参数λ作为惩罚系数，调节惩罚项的大小，表达式如下：
       J(θ) = -sum( yi*(ln h(xi)) + (1-yi)*ln(1-h(xi)) + λ*||θ||1，其中||θ||1为θ的L1范数,
       逻辑回归的L1正则化损失函数的优化方法常用的有坐标轴下降法和最小角回归法
       
    (2)L2正则化
       J(θ) = -sum( yi*(ln h(xi)) + (1-yi)*ln(1-h(xi)) + λ*(||θ||2)^2，其中(||θ||2)^2为θ的L2范数,
       逻辑回归的L2正则化损失函数的优化方法和普通的逻辑回归类似，用梯度下降法
       
 2.二元逻辑回归的推广：多元逻辑回归
    其实这个就涉及到了二分类模型到多分类模型的转变，一个经典的思想就是，one-vs-rest，简称OvR，即总是认为某种类型为正例，其余为负例
    
    这里的多元逻辑回归，主要是结合SoftMax函数，进行推导
"""
