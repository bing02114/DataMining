import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置简体中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 两个类的数据数量
class1_count = 100
class2_count = 259

# 类别标签
labels = ['电动车', '非电动车']

# 数据数量
data_counts = [class1_count, class2_count]

# 绘制水平条形图
fig, ax = plt.subplots(figsize=(7, 3))
ax.barh(labels, data_counts, height=0.4, align='center', color='lightblue', alpha=1)
ax.set_xlabel('数据条数')
ax.set_ylabel('类别')
ax.set_xlim([0, max(data_counts)*1.1])

ax.set_title('两类之间的数据条数对比')
# 调整子图参数，增大周围空白区域
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# 自动调整子图布局
plt.tight_layout()
plt.show()
