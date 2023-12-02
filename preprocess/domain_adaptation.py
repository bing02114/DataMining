import os
import numpy as np
'''
时域转换为频域，FFT
'''

def time2feq(folder_path):
    for root, dirs, files in os.walk(folder_path):
        print("开始将 "+folder_path+" 中的数据转换至频域")
        for file_name in files:
            print ("当前文件名:", folder_path+"/"+file_name)
            # 获取数据
            data_List = read_data_file(folder_path+"/"+file_name)
            if not data_List:
                frequency_domain_data = []
            # 转换频域
            else:
                frequency_domain_data = np.fft.fft(data_List)
            # 新地址
            save_folder_path = folder_path.replace("raw_time_domain","freq_domain")
            print("频域文件名："+save_folder_path+"/"+file_name)
            save_path = save_folder_path+"/"+file_name
            # 保存文件
            save_file(save_path,frequency_domain_data)

# 读取.data文件
def read_data_file(file_path):
    data_list = []  # 存放所有数据的列表
    with open(file_path, 'r') as f:
        data = f.read().splitlines()  # 读取文件中的数据并按行分割
        data = [int(value) for value in data]  # 将数据转换为数值类型（假设数据是浮点数）
        data_list.extend(data)  # 将数据添加到列表中
    return data_list


def save_file(file_path,data_List):
    s=""
    for value in data_List:
        s = s + str(value) + "\n"
    with open(file_path,'w') as f:
        f.write(s)

def main():
    time2feq("../data/raw_time_domain/test")
    time2feq("../data/raw_time_domain/train/EV")
    time2feq("../data/raw_time_domain/train/nEV")

if __name__ == "__main__":
    main()
