import logging

# 配置日志记录
logging.basicConfig(
    filename='testlog.log',  # 日志文件名
    level=logging.DEBUG,  # 日志级别
    format='%(asctime)s - %(levelname)s - %(message)s'  # 日志格式
)

def main():
    logging.info('程序开始运行')
    try:
        a = 0
        b = 1
        result = a + b
        logging.debug(f'计算结果: {a} + {b} = {result}')
        # 警告
        if b == 1:
            logging.warning('警告,b 的值为 1')
        # 错误
        if a == 0:
            raise ValueError('a 的值不能为 0')
    except Exception as e:
        logging.error(f'发生错误: {e}')
    
    logging.info('程序结束运行')

if __name__ == '__main__':
    main()
