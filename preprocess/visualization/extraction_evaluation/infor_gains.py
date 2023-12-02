import math
import pandas as pd

# 从csv文件中读取数据
df = pd.read_csv("../../../data/feature/train/data.csv")

def calculate_entropy(data):
    # 统计各类别样本数量
    label_counts = {}
    for label in data:
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1

    entropy = 0.0
    total_samples = len(data)
    for label in label_counts:
        # 计算每个类别的概率
        prob = float(label_counts[label]) / total_samples
        # 计算熵
        entropy -= prob * math.log(prob, 2)

    return entropy


def calculate_conditional_entropy(data, attribute):
    attribute_values = {}
    for _, row in data.iterrows():
        attr_value = row[attribute]
        if attr_value not in attribute_values:
            attribute_values[attr_value] = []
        attribute_values[attr_value].append(row[-1])

    conditional_entropy = 0.0
    total_samples = len(data)
    for attr_value in attribute_values:
        sub_data = attribute_values[attr_value]
        # 计算子集占比
        prob = float(len(sub_data)) / total_samples
        # 计算子集的条件熵
        sub_entropy = calculate_entropy(sub_data)
        conditional_entropy += prob * sub_entropy

    return conditional_entropy


def calculate_information_gain(data, attribute):
    # 计算数据集的熵
    entropy = calculate_entropy(data.iloc[:, -1])
    # 计算给定属性下的条件熵
    conditional_entropy = calculate_conditional_entropy(data, attribute)
    # 计算信息增益
    information_gain = entropy - conditional_entropy
    return information_gain


# 计算每个属性的信息增益
attributes = list(df.columns[:-1])
information_gains = {}
for attribute in attributes:
    information_gains[attribute] = calculate_information_gain(df, attribute)

# 输出结果
print(information_gains)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置简体中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题
keys = list(information_gains.keys())
values = list(information_gains.values())
plt.figure(figsize=(10, 6))
# 创建柱状图
plt.bar(keys, values)

plt.xticks(rotation=45)
# 设置横轴标签和纵轴标签
plt.xlabel('属性')
plt.ylabel('信息增益')

# 设置标题
plt.title('属性与信息增益')
# 调整子图参数，增大周围空白区域
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# 自动调整子图布局
plt.tight_layout()
# 显示图形
plt.show()