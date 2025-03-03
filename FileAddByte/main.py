

import os
import time
import struct
from datetime import datetime
import threading
from concurrent.futures import ThreadPoolExecutor
import logging

from Config import *

def get_Files_Name(root_dir, suffix_list):
    """
    获取指定目录下特定后缀文件（支持深度控制）

    :param root_dir: 搜索的根目录路径
    :param suffix_list:   需要进行操作的后缀列表（不带点，如"mp4"）
    :param max_depth: 最大遍历深度（0=仅当前目录，1=当前+一级子目录）
    :return: 符合条件的文件路径列表
    """
    file_list = []
    root_dir = os.path.normpath(root_dir)  # 规范化路径

    #当topdown=True时，首先返回根目录下的文件，再遍历子目录；而False时则相反。
    for root, dirs, files in os.walk(root_dir, topdown=True):
        # 计算当前深度
        current_depth = root[len(root_dir):].count(os.path.sep)
        # 深度控制逻辑
        if max_depth is not None and current_depth > max_depth:
            del dirs[:]  # 清空待遍历目录
            continue

        # 过滤文件
        for file in files:
            for suffix in suffix_list:
                if file.lower().endswith(f".{suffix.lower()}"):
                    file_list.append(os.path.join(root, file))
        # 提前终止遍历（当达到最大深度时）
        if max_depth is not None and current_depth == max_depth:
            del dirs[:]  # 阻止继续深入

        if exclude_dirs:
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

    return file_list
def set_time_byte(add_byte):
    '''
    写入一个文件的特征码
    :param add_byte: 添加多大MB数据
    :return:         特征码 + 时间戳  + 写入字节大小 + 结束特征码
    '''
    # 生成时间戳（Unix 时间戳，精确到毫秒）
    #current_time = int(time.time() * 1000)  # 13位整数，占用 8 字节（64位）
    current_time = datetime.fromtimestamp(time.time()) # 13位整数，占用 8 字节（64位）
    current_time = int(current_time.timestamp() * 1000)
    # 将时间戳转换为字节（小端序）
    time_bytes = struct.pack('<Q', current_time)  # 8字节，剩余4字节填充（示例填充0x00）
    # 将 add_byte 转换为 4 字节的小端序二进制数据
    add_byte_bytes = struct.pack('<I', add_byte)  # 小端序，I 表示 4 字节无符号整数
    # 组合完整数据
    data = b'\xff\xfa' + time_bytes + add_byte_bytes + b'\xff\xff'
    return data
    # with open('test', 'ab') as f:
    #     f.write(data)


def get_time_byte(file_name):
    """
    读取文件最后16字节，验证特征码并解析时间戳和填充量
    :param file_name: 文件名
    :return: None
    """
    try:
        # 获取文件大小
        file_size = os.path.getsize(file_name)
        if file_size < 16:
            print(f"错误：文件 {file_name} 大小不足16字节")
            return

        # 直接读取最后16字节
        with open(file_name, 'rb') as f:
            f.seek(-16, os.SEEK_END)  # 定位到倒数第16字节位置
            data = f.read(16)

        # 验证特征码
        if data[0:2] != b'\xff\xfa' or data[-2:] != b'\xff\xff':
            print(f"文件 {file_name} 特征码不匹配")
            return

        # 解析数据
        time_bytes = data[2:10]  # 提取8字节时间戳
        add_byte_bytes = data[10:14]  # 提取4字节填充量

        timestamp = int.from_bytes(time_bytes, byteorder='little')
        add_byte = struct.unpack('<I', add_byte_bytes)[0]

        # 转换为可读时间（东八区）
        dt = datetime.fromtimestamp(timestamp / 1000)
        print(f"{file_name}:\n最后写入时间（本地）: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"最后填充大小: {add_byte} MB")

    except FileNotFoundError:
        print(f"文件 {file_name} 不存在")
    except PermissionError:
        print(f"无权限读取文件 {file_name}")
    except Exception as e:
        print(f"处理文件 {file_name} 时发生异常: {str(e)}")


# 配置日志记录，记录异常信息
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
lock = threading.Lock()  # 用于线程安全的打印输出


def process_file(file_name, add_byte):
    '''
    写入随机数据到该文件内
    :param file_name:文件路径
    :param add_byte:添加的大小(MB)
    :return:
    '''
    try:
        with open(file_name, 'ab') as f:
            # 写入随机数据
            f.write(os.urandom(1024 * 1024 * add_byte))
            # 写入时间戳和添加字节大小 特征码
            f.write(set_time_byte(add_byte))
        # 加锁确保打印内容不混乱
        with lock:
            print(f"{file_name} 写入 {add_byte} MB 成功！")
        return True
    except FileNotFoundError as e:
        logging.error(f"文件 {file_name} 不存在：{e}")
    except PermissionError as e:
        logging.error(f"无权限写入 {file_name}：{e}")
    except OSError as e:
        logging.error(f"系统错误：{e}")
    except Exception as e:
        logging.error(f"未知异常：{e}")
    return False


def write_byte(files_name, add_byte, max_workers=50):
    '''
    利用多线程写入文件内容
    :param files_name: 文件路径
    :param add_byte: 添加的大小(MB)
    :param max_workers: 线程大小
    :return:
    '''
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_file, file, add_byte) for file in files_name]

    success, failed = 0, 0
    for future in futures:
        if future.result():
            success += 1
        else:
            failed += 1
    end_time = time.time()
    print(f"任务完成：成功 {success} 个，失败 {failed} 个")
    print(f"写入{add_byte}MB成功！耗时：{end_time-start_time}秒！")

if __name__ == '__main__':
    # 获取文件列表
    files_name = get_Files_Name(root_dir, suffix_list)
    # 写入文件
    write_byte(files_name, add_byte)

    # 验证文件
    #for _ in files_name:
    #    get_time_byte(_)