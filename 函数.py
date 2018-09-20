import functools
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')#必填在前
#默认参数必须指向不可变对象
def calc(*numbers):#不定长参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):#关键字参数
    print('name:', name, 'age:', age, 'other:', kw)

def person(name, age, *, city, job):#命名关键字参数
    print(name, age, city, job)

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])#map()函数
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)#这个函数必须接收两个参数
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))#自带bool()

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

def lazy_sum(*args):#返回函数
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1,2,3)
print(f())

def add(x,y):#返回函数
	return x+y
def a(*args):
	def b():
		return reduce(add,list(args))
	return b
x=a(1,2,3)
print(x())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()

list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

int2 = functools.partial(int, base=2)
int2('1000000')#64

max2 = functools.partial(max, 10)#args = (10, 5, 6, 7) max(*args)

def f():
    global x
    return None
