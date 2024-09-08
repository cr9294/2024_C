import numpy as np
import matplotlib.pyplot as plt

# 假设次品率服从 Beta 分布
#alpha, beta = 2, 8  # 先验分布参数，可以根据实际情况调整 20%
#alpha, beta = 5, 95  # 先验分布参数，可以根据实际情况调整 5%
alpha, beta = 2, 18  # 先验分布参数，可以根据实际情况调整 10%
n_simulations = 10000  # 模拟次数

# 生成次品率的模拟值
defective_rates = np.random.beta(alpha, beta, n_simulations)

# 假设每批产品的数量为100，计算每次模拟的次品数量
batch_size = 100
defective_counts = np.random.binomial(batch_size, defective_rates)

# 绘制模拟结果的直方图
plt.hist(defective_counts, bins=30, alpha=0.7, color='b', label="Defective Count Distribution")
plt.xlabel("Number of Defective Products per Batch")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation of Defective Counts")
plt.show()

# 计算次品率的平均值和标准差
mean_defective_rate = np.mean(defective_rates)
std_defective_rate = np.std(defective_rates)

print(f"平均次品率: {mean_defective_rate:.2%}")
print(f"次品率标准差: {std_defective_rate:.2%}")
