import pandas as pd

brics = pd.read_csv('./jpginfo.csv', index_col=0)
print(brics)

# 获取列
# 类似js中的对象
print(brics['checksum'])

# 添加列
brics['comment'] =  brics['checksum']
print(brics)

# 获取行
# print(brics.loc["002"])