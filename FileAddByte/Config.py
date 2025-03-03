import configparser

# 创建配置解析器
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')  # 指定编码避免乱码

# 添加的目录
root_dir = config.get('Settings', 'rootDir')

# 解析的后缀名
suffix = config.get('Settings', 'suffix')
suffix_list = [s.strip() for s in suffix.split(',')]

# 获取参数
add_byte = config.getint('Settings', 'addByte')  # 直接转为整数

# 解析排除目录（需字符串转列表）
exclude_dirs_str = config.get('Settings', 'exclude_dirs')
exclude_dirs = [d for d in exclude_dirs_str.split(',') if d.strip()]

# 爬取深度
try:
    max_depth = config.getint('Settings', 'max_depth')
except Exception as e:
    max_depth = None

