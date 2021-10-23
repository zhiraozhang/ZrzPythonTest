#比较大小函数
def max(a, b):
    if a >= b:
        print("a的值更大")
        return a
    else:
        print("b的值更大")
        return b
if __name__ == '__main__' :
    a = input("请输入a：")
    int(a)
    print('a的值为', a)
    print('-------------')
    b=input('请输入b；')
    int(b)
    print('b的值为', b)
    print('-------------')
    print('最大值为', max(a, b))
    print('-----End-----')
