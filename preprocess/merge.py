import pandas as pd
import numpy as np

def merge():
    # 读取两个CSV文件
    df1 = pd.read_csv('../data/feature/EV/data.csv')
    df2 = pd.read_csv('../data/feature/nEV/data.csv')

    # 添加标签列并设置对应的值
    # df1 = df1[['频率熵'],['频域能量'],['峰值频率'],['峰值'],['均值'],['标准差'],['标签']]
    # df2 = df2[['频率熵'],['频域能量'],['峰值频率'],['峰值'],['均值'],['标准差'],['标签']]

    df1['标签'] = 1
    df2['标签'] = 0

    # 合并两个DataFrame
    merged_df = pd.concat([df1, df2])

    # 打乱数据顺序
    shuffled_index = np.random.permutation(merged_df.index)
    shuffled_df = merged_df.loc[shuffled_index]

    # 保存合并且打乱顺序后的结果到新的CSV文件
    shuffled_df.to_csv('../data/feature/train/data.csv',index=False,header=True)

def main():
    merge()

if __name__ == "__main__":
    main()
