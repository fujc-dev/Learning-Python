# 定义函数关键字 def
# 函数、循环、判断都是以没有缩进表示结束


def say_hello(name):
    print('{0},Hello!'.format(name))


say_hello("LiLei")


# 类
class YTSolver:
    # 构造函数
    def __init__(self, name):
        self.name = name

    # 打印名称
    def print_name(self):
        print('{0},Hello!'.format(self.name))


_ = YTSolver("zhangsan")
_.print_name()


# 继承

class A:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_string(self):
        print("class A---id:{0},name:{1}".format(self.id, self.name))


class B(A):
    def __init__(self, id, name, nickname):
        A.__init__(self, id, name)
        self.nickname = nickname

    def to_string_extend(self):
        A.to_string(self);
        print("class B---id:{0},name:{1},nickname:{2}".format(self.id, self.name, self.nickname))


# 调用方式

a = A(1, 'zhangsan')
a.to_string()
print("==============================分割线==============================")
b = B(1, 'lisi', 'zzz')
b.to_string_extend()
