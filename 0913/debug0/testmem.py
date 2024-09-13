from memory_profiler import profile

@profile
def example_function():
    # 大列表占用内存
    large_list = [i for i in range(100000)]
    return large_list

if __name__ == '__main__':
    example_function()
