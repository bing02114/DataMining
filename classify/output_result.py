import csv

def result(predictions,file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # 将预测结果填入CSV文件的第二列
    for i in range(len(predictions)):
        data[i+1][1]=predictions[i]

    # data[105][1]=0

    # 写入更新后的内容到CSV文件
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)