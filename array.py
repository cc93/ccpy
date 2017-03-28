import numpy

height = numpy.array([1.73, 1.68, 1.71, 1.89, 1.79])
weight = numpy.array([65.4, 59.2, 63.6, 88.4, 68.7])
strArr = numpy.array(['str', 65.4, 59.2, 63.6, 88.4, 68.7])

print('1.numpy的array是对元素逐个操作')
print(weight / height ** 2)
print(weight + height)
print('而Python的list是对list整体操作')
list1 = [1.73, 1.68, 1.71, 1.89, 1.79]
list2 = [65.4, 59.2, 63.6, 88.4, 68.7]
print(list1 + list2)

print('2.一个array中只能有一种类型，但一个list可以装多个类型')
print(numpy.array([1.73, 1.68, 1.71, 1.89, 1.79, 'cc']))
print([1.73, 1.68, 1.71, 1.89, 1.79, 'cc'])

print('3.可以构建不等式来选取元素')
print(weight[weight > 60])

print('4.多维数组-->类似于MATLAB的多维向量')
arr_2d = numpy.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                      [65.4, 59.2, 63.6, 88.4, 68.7]])
print(arr_2d)
# （2,5） 两行五列
print(arr_2d.shape)
# 63.6
print(arr_2d[1, 2])
print(arr_2d[1][2])
"""
[[  1.68   1.71]
 [ 59.2   63.6 ]]
"""
print(arr_2d[:,1:3])
# 多维数组也可进行逐个元素的计算
print(arr_2d ** 2)

print('array在数据运算中的好处：比list快，因为array中存储的数据都是同一种数据类型')