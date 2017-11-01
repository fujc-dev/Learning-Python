# -*- coding:UTF-8 -*-
#
#
#

class Fruits(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # @staticmethod 把没有参数的函数装饰过后变成可以被类实例调用的函数，函数定义时是没有参数的。
    # @classmethod 把装饰过的方法变成一个classmethod类对象，既能被类调用又能被类实例调用，
    #   但是被装饰的方法需要传递一个cls参数用于表示类本身。
    # @property 装饰过的函数不在是一个函数，而是一个property，装饰过的方法不再是可调用的方法，可以看作对象属性访问
    @property
    def show(self):
        print "name：" + self.name + " color：" + self.color

    def __str__(self):
        return "这个有点类似于重写Java里面的ToString方法"

    def __repr__(self):
        return "重写返回内存地址"


_apple = Fruits("苹果", "red")
_apple.show
print _apple
