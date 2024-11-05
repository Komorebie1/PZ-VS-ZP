import subprocess

# 定义要运行的两个Python文件路径
script1 = "player1.py"
script2 = "player2.py"

# 使用subprocess启动两个独立的进程
process1 = subprocess.Popen(["python", script1])
process2 = subprocess.Popen(["python", script2])

# 等待两个进程完成（可选）
process1.wait()
process2.wait()

print("Both scripts have finished running.")
