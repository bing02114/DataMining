import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from classify.output_result import result
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

# 从CSV文件加载数据
data = pd.read_csv('../data/feature/train/data.csv')
data_test = pd.read_csv('../data/feature/test/data.csv')

# 提取特征和标签
X = data.iloc[:, :-1]  # 提取所有行，除了最后一列之外的所有列作为特征
y = data.iloc[:, -1]   # 提取最后一列作为标签

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 定义参数
param = {
    'max_depth': 4,
    'eta': 0.001,
    'objective': 'binary:logistic',
    'min_child_weight': 20,
    'subsample': 0.9,
    'colsample_bytree': 0.5,
    'gamma': 0.1,
    'alpha': 0.1,
    'lambda': 0.1,
    'scale_pos_weight':2.59
}

# 将训练集和测试集转换为DMatrix格式
dtrain = xgb.DMatrix(data=X_train, label=y_train)
dtest = xgb.DMatrix(data=X_test, label=y_test)
test = xgb.DMatrix(data=data_test)
# 训练模型
num_round = 10000  # 迭代次数
bst = xgb.train(param, dtrain, num_round)

# 模型预测
pred = bst.predict(dtest)
pred_binary = [1 if p > 0.5 else 0 for p in pred]

# 计算准确度、精确度、召回率和F1值
accuracy = accuracy_score(y_test, pred_binary)
precision = precision_score(y_test, pred_binary)
recall = recall_score(y_test, pred_binary)
f1 = f1_score(y_test, pred_binary)

print("准确度：", accuracy)
print("精确度：", precision)
print("召回率：", recall)
print("F1值：", f1)

pred_z = bst.predict(test)
predz_binary = [1 if p > 0.53 else 0 for p in pred_z]


result(predz_binary,'../result/bst.csv')

