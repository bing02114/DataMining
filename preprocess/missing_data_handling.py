import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

'''
处理数据缺失值，拉格朗日插值
'''
# 拉格朗日插值填充缺失值
def interpolate_missing_values(data):
    # 找到缺失值的位置
    missing_indices = np.where(np.isnan(data))[0]

    # 如果数据中没有缺失值，则直接返回
    if len(missing_indices) == 0:
        return data

    # 找到缺失值的左右两侧位置
    start_index = missing_indices[0] - 1
    end_index = missing_indices[-1] + 1

    # 去除缺失值
    x_known = np.delete(np.arange(len(data)), missing_indices)
    y_known = np.delete(data, missing_indices)
    # 计算拉格朗日插值多项式
    poly = interp1d(x_known, y_known, kind='quadratic')

    # 计算新x值上的估计y值
    x_new = np.arange(start_index, end_index + 1)
    y_new = poly(x_new)

    # 处理为int
    modified_values = []
    for value in y_new:
        modified_value = "{}.0".format(int(value))
        modified_value = int(float(modified_value))
        modified_values.append(modified_value)
    y_new = modified_values

    # 将插值结果替换回原始数组
    data[start_index + 1:end_index] = y_new[1:-1]

    return data

# 读取数据
def read_data_file(file_path):
    data_list = []  # 存放所有数据的列表
    with open(file_path, 'r') as f:
        data = f.read().splitlines()  # 读取文件中的数据并按行分割
        for value in data:
            if value == "?":
                value = -10000
        data = [int(x) if x != '?' else np.nan for x in data]  # 将数据转换为数值类型（假设数据是浮点数）
        data_list.extend(data)  # 将数据添加到列表中
    return data_list

# 保存数据
def save_file(file_path,data_List):
    s=""
    for value in data_List:
        s = s + str(value) + "\n"
    with open(file_path,'w') as f:
        f.write(s)

# 打印图片
def print_plot(list):
    plt.plot(list)  # 绘制折线图
    plt.xlabel('time')
    plt.ylabel('data')  # 设置纵轴标题
    plt.show()  # 显示图形

def main():
    data_file1 = "../data/raw_time_domain/train/EV/1686116040i.data"
    data_file2 = "../data/raw_time_domain/test/89.data"
    data1 = interpolate_missing_values(read_data_file(data_file1))
    data2 = interpolate_missing_values(read_data_file(data_file2))
    save_file(data_file1,data1)
    save_file(data_file2,data2)

if __name__ == "__main__":
    main()