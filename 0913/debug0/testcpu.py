import cProfile
import pstats
import io

def example_function():
    # 示例函数：计算前10000个数的平方和
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

def profile_function(func):
    pr = cProfile.Profile()
    pr.enable()
    func()
    pr.disable()
    
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

if __name__ == '__main__':
    profile_function(example_function)
