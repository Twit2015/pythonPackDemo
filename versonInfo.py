# import sys
# print(sys.version_info)
# # bytes  ASCII
# a = b'h\x65llo'
# print(list(a))
# print(a)
# # str Unicode code point
# a1= 'a\u0300 propos'
# print(list(a1))
# print(a1)

# def to_str(bytes_or_str):
#     if isinstance(bytes_or_str,bytes):
#         value = bytes_or_str.decode('utf-8')
#     else:
#         value = bytes_or_str
#     return value   # Instance of str
# print(repr(to_str(b'foo')))
# print(repr(to_str('bar')))
#
# def to_bytes(bytes_or_str):
#     if isinstance(bytes_or_str,str):
#         value = bytes_or_str.encode('utf-8')
#     else:
#         value = bytes_or_str
#     return value  # Instance of bytes
#
# print(repr(to_bytes(b'foo')))
# print(repr(to_bytes('bar')))
#
# assert b'red' > b'blue'
# assert 'red' > 'blue'
# assert b'red' > b'blue'
# print(b'foo' =='foo')

# import locale
# print(locale.getpreferredencoding())  # UTF-8
# a2 = 1234.5679
# # Effective Python  rule 4 内置的format函数与str类的format方法
# formatted = format(a2, ',.2f')
# print(formatted)
# b2 = 'hello inner format function'
# formatted1 = format(b2,'^30s')
# print("*",formatted1,"*")
#
# key = 'my_variable'
# value = 12.3456
# formatted3 = f'{key} = {value:.2f}'
# print(formatted3)

# # 用辅助函数取代复杂的表达式
# from urllib.parse import parse_qs
# my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
# print(repr(my_values))
# # unpacking 机制
# item = ('Peanut butter','Jelly')
# first,second = item  # Unpacking
# print(first, 'and', second)
#
# # enumerate 代替range
# flavor_list =['vanilla','chocolate','pecan','strawberry']
# for flavor in flavor_list:
#     print(f'{flavor} is  delicious')
#
# for i, flavor in enumerate(flavor_list):
#     print(f'{i+ 1}:{flavor}')
#
# for i, flavor in enumerate(flavor_list,2):  # 指定下标从2开始，默认从0开始
#     print(f'{i}:{flavor}')

# # zip 用zip函数同时遍历两个迭代器
# names = ['Cecilia', 'Lise', 'Marie']
# counts = [len(word) for word in names]
# print(counts)
# longest_name = None
# max_count = 0
# for name, count in zip(names, counts):
#     if count > max_count:
#         longest_name = name
#         max_count = count
# print(longest_name)
# names.append('TomHahaha')
#
# import  itertools
# for name, count in itertools.zip_longest(names, counts):
#     print(f'{name}:{count}')


# assignment expression

# 学会对序列做切片 切割时所用的下标可以越界
# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print('Middle two:  ', a[3:5])
# print('All but ends:', a[1:7])
# print('All but ends:', a[0:4])
# print('All but ends:', a[:4])
# print('All but ends:', a[3:8])
# print('All but ends:', a[3:])
# print('All but ends:', a[3:len(a)])
# print('All but ends:', a[3:-1])
# print('All but ends:', a[-3:-1])
# print('All but ends:', a[-len(a):-1])
# print('All but ends:', a[-len(a):])

# x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# odds = x[::2]
# evens = x[1::2]
# print(odds)
# print(evens)
#
# # 反转字符串
# x = b'thisisaquestion'
# y = x[::-1]
# print(y)
# # Unicode字符串也可以这么反转
# x = '寿司'
# y = x[::-1]
# print(y)
# UTF-18字符串这么反转不灵了！
# x1 = '寿司'
# x2 = x1.encode('utf-8')
# y1 = x2[::-1]
# print(y1.decode('utf-8'))
import numpy as np

arr1 = np.array([[0., 0., 0.], [1., 1., 1.]])
print(arr1)
print(arr1.shape)
print(arr1.flags)
print(arr1.strides)
print(arr1.ndim)
print(arr1.size)
print(arr1.data)
print(arr1.dtype)