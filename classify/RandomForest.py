import sys

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from classify.output_result import result
import pandas as pd

# 1. 准备数据集
data = pd.read_csv('../data/feature/train/data.csv')
data_test = pd.read_csv('../data/feature/test/data.csv')
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
# 2. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

# 3. 创建随机森林模型
rf_model = RandomForestClassifier(
    n_estimators=3,
    criterion='entropy',
    max_depth=3,
    min_samples_split=30,
    min_samples_leaf=10,
    max_features='sqrt',
    bootstrap=True,
    random_state=42,
    class_weight={0:1,1:2},
    oob_score=False)

# 4. 训练模型
rf_model.fit(X_train, y_train)

# 5. 预测
y_pred = rf_model.predict(X_test)

# 6. 评估模型
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("准确度：", accuracy)
print("精确度：", precision)
print("召回率：", recall)
print("F1值：", f1)

z_pred = rf_model.predict(data_test)

result(z_pred,'../result/rf.csv')

