import matplotlib.pyplot as plt
import os
import numpy as np

'''
原始数据可视化，画出时域波形图
'''
# .data -> .png
def data2fig(folder_path,save_path):
    for root, dirs, files in os.walk(folder_path):
        print("开始将 "+folder_path+" 中的原始数据可视化")
        for file_name in files:
            print("当前文件名:", file_name)
            data_List = read_data_file(folder_path+"/"+file_name)
            fig_path = file_name.rstrip(".data")
            save_plot(data_List,save_path,fig_path+".png",len(data_List))

# 读取.data文件
def read_data_file(file_path):
    data_list = []  # 存放所有数据的列表
    with open(file_path, 'r') as f:
        data = f.read().splitlines()  # 读取文件中的数据并按行分割
        # 将数据转化为复数
        complex_data = [complex(d) for d in data]
        # 获得幅度谱图
        data = np.abs(complex_data)
        data_list.extend(data)  # 将数据添加到列表中
    return data_list

# 画出图形
def print_plot(list):
    plt.plot(list)  # 绘制折线图
    plt.xlabel('time')
    plt.ylabel('data')  # 设置纵轴标题
    plt.show()  # 显示图形

# 画出并保存图形
def save_plot(list,file_path,file_name,length):
    plt.figure()

    plt.plot(list)  # 绘制折线图
    plt.xlabel('freq')
    plt.ylabel('data')  # 设置纵轴标题
    output_file = os.path.join(file_path,file_name)  # 构建输出文件路径
    plt.savefig(output_file)  # 保存图形到文件中
    plt.close()


def main():
    data2fig("../../../data/freq_domain/train/nEV", "../../fig/freq/nEV")
    data2fig("../../../data/freq_domain/train/EV", "../../fig/freq/EV")
    data2fig("../../../data/freq_domain/test", "../../fig/freq/test")
if __name__ == "__main__":
    main()