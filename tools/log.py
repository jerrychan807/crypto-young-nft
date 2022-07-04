'''
@Descripttion: 
@version: 
@Author: duyan
@Date: 2020-07-21 17:54:24
@LastEditors: duyan
@LastEditTime: 2020-07-21 17:54:39
'''
import sys
import pathlib

from loguru import logger

# 路径设置
relative_directory = pathlib.Path(__file__).parent  # 代码相对路径
result_save_dir = relative_directory.joinpath('log')  # 结果保存目录
log_path = result_save_dir.joinpath('parse.log')  # 日志保存路径

# 日志配置
# 终端日志输出格式
stdout_fmt = '<cyan>{time:HH:mm:ss,SSS}</cyan> ' \
             '[<level>{level: <5}</level>] ' \
             '<blue>{module}</blue>:<cyan>{line}</cyan> - ' \
             '<level>{message}</level>'
# 日志文件记录格式
logfile_fmt = '<light-green>{time:YYYY-MM-DD HH:mm:ss,SSS}</light-green> ' \
              '[<level>{level: <5}</level>] ' \
              '<cyan>{process.name}({process.id})</cyan>:' \
              '<cyan>{thread.name: <18}({thread.id: <5})</cyan> | ' \
              '<blue>{module}</blue>.<blue>{function}</blue>:' \
              '<blue>{line}</blue> - <level>{message}</level>'

logger.remove()
logger.level(name='TRACE', color='<cyan><bold>', icon='✏️')

# 如果你想在命令终端静默运行，可以将以下一行中的level设置为QUITE
logger.add(sys.stderr, level='DEBUG', format=stdout_fmt, enqueue=True)  # 命令终端日志级别默认为INFOR
logger.add(log_path, level='DEBUG', format=logfile_fmt, enqueue=True,
           encoding='utf-8')  # 日志文件默认为级别为DEBUG
