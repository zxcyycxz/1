# 导入time模块
import time

# 设置专注时段为50分钟
focus_time = 50 * 60

# 创建一个计时器函数
def timer(seconds):
  # 获取当前时间
  start_time = time.time()
  # 计算结束时间
  end_time = start_time + seconds
  # 循环直到结束时间
  while time.time() < end_time:
    # 计算剩余时间
    remaining_time = end_time - time.time()
    # 格式化剩余时间为时分秒
    hours, minutes, seconds = int(remaining_time // 3600), int(remaining_time % 3600 // 60), int(remaining_time % 60)
    # 打印剩余时间
    print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}", end="")
    # 暂停一秒
    time.sleep(1)
  # 打印结束信息
  print("\n专注时段结束！")

# 调用计时器函数
timer(focus_time)
