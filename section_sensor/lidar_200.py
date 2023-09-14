import pandas as pd
import matplotlib.pyplot as plt
import math
import drawing

#データを読み込む
data = pd.read_csv("sensor_data_200.txt",delimiter=" ",
                   header=None,names=("date","time","ir","lidar"))

#平均値を求める
zs = data["lidar"].values
mean = sum(zs)/len(zs)

#平均からの差の二乗を計算
diff_square = [(z - mean)**2 for z in zs]

#標本分散
sample_var = sum(diff_square) / len(zs)

#不変分散
unbiased_var = sum(diff_square) / (len(zs)-1)

#標準偏差
stddev1 = math.sqrt(sample_var)
stddev2 = math.sqrt(unbiased_var)

#確率分布
freqs = pd.DataFrame(data["lidar"].value_counts())
freqs["probs"] = freqs["lidar"]/len(data["lidar"])

#lidarデータのヒストグラムを描く
#  data["lidar"].hist(bins=max(data["lidar"])-min(data["lidar"]),color="orange",align="left")

#lidarデータの確率分布を描く
#freqs["probs"].sort_index().plot.bar()

#平均値を図へ挿入
#  plt.vlines(mean,ymin=0,ymax=5000,color="red")

#標準偏差の結果を図へ挿入
#  plt.vlines(mean+stddev1, ymin=0,ymax=5000,color="black")
#  plt.vlines(mean-stddev1,ymin=0,ymax=5000,color="black")

#確率分布を基に値をdata数分ドロー
samples = [drawing.drawing(freqs) for i in range(len(data))]
simulated = pd.DataFrame(samples,columns=["lidar"])
p = simulated["lidar"]
#p.hist(bins=max(p)-min(p),color="orange",align="left")

#plt.show()

