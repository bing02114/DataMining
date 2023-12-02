import numpy as np
import pandas as pd
import os
import numpy as np
from scipy.stats import skew, kurtosis

def freq_feature(folder_path):
    result = {
        '频域幅值平均值': [],
        '重心频率': [],
        '均方频率': [],
        '频率方差': [],
        '均方根频率': [],
        '频率幅值方差': [],
        '频域幅值偏度指标': [],
        '频域幅值峭度指标': [],
        '频率标准差': [],
        '频域频率歪度': [],
        '频域频率峭度': [],
        '平方根比率': []
    }
    for root, dirs, files in os.walk(folder_path):
        print("开始将 "+folder_path+" 中的数据进行提取频域特征")
        for file_name in files:
            print ("当前文件名:", folder_path+"/"+file_name)
            # 获取数据
            spec = read_data_file(folder_path+"/"+file_name)
            if not spec:
                result = []
                continue

            amp_mean = np.abs(spec).mean()
            result['频域幅值平均值'].append(amp_mean)

            # 进行FFT变换得到频域幅值谱
            amp_spec = np.fft.fft(np.abs(spec))

            # 计算频域幅值谱的频率特征
            n_samples = len(amp_spec)
            fs=1000
            freqs = np.fft.fftfreq(n_samples, d=1.0 / fs)[:n_samples // 2]
            centroid_freq = np.sum(freqs * amp_spec[:n_samples // 2]) / np.sum(amp_spec[:n_samples // 2])
            result['重心频率'].append(np.abs(centroid_freq))

            freq_var = np.sum((freqs - centroid_freq) ** 2 * amp_spec[:n_samples // 2]) / np.sum(
                amp_spec[:n_samples // 2])
            result['频率方差'].append(np.abs(freq_var))

            rms_freq = np.sqrt(np.sum((freqs ** 2) * amp_spec[:n_samples // 2]) / np.sum(amp_spec[:n_samples // 2]))
            result['均方频率'].append(np.abs(rms_freq))

            rms_amp = np.sqrt(np.mean(np.abs(spec) ** 2))
            result['均方根频率'].append(rms_amp)

            freq_amp_var = np.var(np.abs(spec))
            result['频率幅值方差'].append(freq_amp_var)

            skewness = skew(np.abs(spec))
            result['频域幅值偏度指标'].append(skewness)

            kurt = kurtosis(np.abs(spec))
            result['频域幅值峭度指标'].append(kurt)

            freq_std = np.std(freqs * np.abs(spec)[:n_samples // 2])
            result['频率标准差'].append(freq_std)

            freq_skewness = skew(freqs * np.abs(spec)[:n_samples // 2])
            result['频域频率歪度'].append(freq_skewness)

            freq_kurt = kurtosis(freqs * np.abs(spec)[:n_samples // 2])
            result['频域频率峭度'].append(freq_kurt)

            sqrt_ratio = np.sqrt(np.mean(np.abs(spec[1:]) ** 2) / np.mean(np.abs(spec[:-1]) ** 2))
            result['平方根比率'].append(sqrt_ratio)


    if("train" in folder_path):
        path = folder_path.replace("freq_domain/train","feature")+"/"+"data.csv"
    if("test" in folder_path):
        path = folder_path.replace("freq_domain/test","feature/test")+"/"+"data.csv"

    df = pd.DataFrame(result)
    df.to_csv(path,index=False,header=True)

def freq_feature_test(folder_path):
    result = {
        '频域幅值平均值': [],
        '重心频率': [],
        '均方频率': [],
        '频率方差': [],
        '均方根频率': [],
        '频率幅值方差': [],
        '频域幅值偏度指标': [],
        '频域幅值峭度指标': [],
        '频率标准差': [],
        '频域频率歪度': [],
        '频域频率峭度': [],
        '平方根比率': []
    }
    for i in range(152):
        print("开始将 "+folder_path+" 中的数据进行提取频域特征")
        file_name = str(i)+".data"

        print ("当前文件名:", folder_path+"/"+file_name)
        # 获取数据
        spec = read_data_file(folder_path+"/"+file_name)
        if not spec:
            result['频域幅值平均值'].append(0)
            result['重心频率'].append(0)
            result['频率方差'].append(0)
            result['均方频率'].append(0)
            result['均方根频率'].append(0)
            result['频率幅值方差'].append(0)
            result['频域幅值偏度指标'].append(0)
            result['频域幅值峭度指标'].append(0)
            result['频率标准差'].append(0)
            result['频域频率歪度'].append(0)
            result['频域频率峭度'].append(0)
            result['平方根比率'].append(0)
            continue
        amp_mean = np.abs(spec).mean()
        result['频域幅值平均值'].append(amp_mean)

        # 进行FFT变换得到频域幅值谱
        amp_spec = np.fft.fft(np.abs(spec))

        # 计算频域幅值谱的频率特征
        n_samples = len(amp_spec)
        fs=1000
        freqs = np.fft.fftfreq(n_samples, d=1.0 / fs)[:n_samples // 2]
        centroid_freq = np.sum(freqs * amp_spec[:n_samples // 2]) / np.sum(amp_spec[:n_samples // 2])
        result['重心频率'].append(np.abs(centroid_freq))

        freq_var = np.sum((freqs - centroid_freq) ** 2 * amp_spec[:n_samples // 2]) / np.sum(
             amp_spec[:n_samples // 2])
        result['频率方差'].append(np.abs(freq_var))

        rms_freq = np.sqrt(np.sum((freqs ** 2) * amp_spec[:n_samples // 2]) / np.sum(amp_spec[:n_samples // 2]))
        result['均方频率'].append(np.abs(rms_freq))

        rms_amp = np.sqrt(np.mean(np.abs(spec) ** 2))
        result['均方根频率'].append(rms_amp)

        freq_amp_var = np.var(np.abs(spec))
        result['频率幅值方差'].append(freq_amp_var)

        skewness = skew(np.abs(spec))
        result['频域幅值偏度指标'].append(skewness)

        kurt = kurtosis(np.abs(spec))
        result['频域幅值峭度指标'].append(kurt)

        freq_std = np.std(freqs * np.abs(spec)[:n_samples // 2])
        result['频率标准差'].append(freq_std)

        freq_skewness = skew(freqs * np.abs(spec)[:n_samples // 2])
        result['频域频率歪度'].append(freq_skewness)

        freq_kurt = kurtosis(freqs * np.abs(spec)[:n_samples // 2])
        result['频域频率峭度'].append(freq_kurt)

        sqrt_ratio = np.sqrt(np.mean(np.abs(spec[1:]) ** 2) / np.mean(np.abs(spec[:-1]) ** 2))
        result['平方根比率'].append(sqrt_ratio)


    if("train" in folder_path):
        path = folder_path.replace("freq_domain/train","feature")+"/"+"data.csv"
    if("test" in folder_path):
        path = folder_path.replace("freq_domain/test","feature/test")+"/"+"data.csv"

    df = pd.DataFrame(result)
    df.to_csv(path,index=False,header=True)

def read_data_file(file_path):
    data_list = []  # 存放所有数据的列表
    with open(file_path, 'r') as f:
        data = f.read().splitlines()  # 读取文件中的数据并按行分割
        for value in data:
            if value == "?":
                value = -10000
        data = [complex(value) for value in data]  # 将数据转换为数值类型（假设数据是浮点数）
        data_list.extend(data)  # 将数据添加到列表中
    return data_list

def main():
    freq_feature("../../data/freq_domain/train/EV")
    freq_feature("../../data/freq_domain/train/nEV")
    freq_feature_test("../../data/freq_domain/test")

if __name__ == "__main__":
    main()