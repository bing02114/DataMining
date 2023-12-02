import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 读取两个csv文件
df1 = pd.read_csv('../../../data/feature/EV/data.csv')
df2 = pd.read_csv('../../../data/feature/nEV/data.csv')
df3 = pd.read_csv('../../../data/feature/test/data.csv')

plt.rcParams['font.family'] = 'Microsoft YaHei'

# 获取需要绘制的属性
def print_point(col_name):
    x_col = col_name
    y_col = col_name
    # plt.figure()
    # 绘制csv文件的散点图
    plt.scatter(df2[x_col], df2[y_col], label='nEV')
    plt.scatter(df1[x_col], df1[y_col], label='EV')
    # plt.scatter(df3[x_col], df3[y_col], label='test')

    # 设置图例和坐标轴标签
    plt.legend()
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    # 显示图形
    plt.show()
    # plt.close()

def print_box(col_name):

    # 读取CSV文件
    dataEV = pd.read_csv('../../../data/feature/EV/data.csv')
    dataNEV = pd.read_csv('../../../data/feature/nEV/data.csv')
    # 提取需要对比的两组数据的属性列
    data1 = dataEV[col_name]
    data2 = dataNEV[col_name]

    # 数据集合
    data = [data1, data2]

    # 创建箱线图
    plt.boxplot(data)

    # 设置x轴刻度标签
    plt.xticks([1, 2], ['Data 1', 'Data 2'])

    # 坐标轴长度
    plt.xlim(0, 500000)  # 设置x轴范围
    plt.ylim(0, 500000)  # 设置y轴范围
    # 添加标题和坐标轴标签
    plt.title('Box Plot')
    plt.xlabel('Data')
    plt.ylabel('Values')

    # 显示图形
    plt.show()


def main():
    data_list = [        '频域幅值平均值',
        '重心频率',
        '均方频率',
        '频率方差',
        '均方根频率',
        '频率幅值方差',
        '频域幅值偏度指标',
        '频域幅值峭度指标',
        '频率标准差',
        '频域频率歪度',
        '频域频率峭度',
        '平方根比率']
    # '频率熵','频域能量', '峰值', '均值', '标准差'
    for data in data_list:
        print_point(data)
        # print_box(data)

if __name__ == "__main__":
    main()