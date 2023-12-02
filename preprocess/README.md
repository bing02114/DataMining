### 数据预处理
* feature_extraction 特征提取
* fig 波形图/幅度图
* visualization 可视化

* domain_adaptation.py 时域->频域
* merge 构造训练集
* missing_data_handling.py 遗失数据处理

#### 遗失数据处理
1. 对于训练集中的部分数据缺失，采用拉格朗日插值进行填充
2. 对于测试集中的空文件，采用填充0的方式处理