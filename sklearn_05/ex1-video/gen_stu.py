'''
生成器，使用 yield 关键字返回的函数，返回一个序列。
每调用一次就返回一次，返回后生成器函数不停止，继续运行到下次返回(yield)之前
'''
print(range(10))

for i in range(10):
    print(i)

# 生成器函数(带yield)
def myrange(num):
    i = 0
    while i < num:
        yield i
        i += 1

for i in myrange(5):
    print(i)

res = myrange(5)
print(res)
for i, c in enumerate(res):
    print(c)