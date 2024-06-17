# Titanfall 2 Server Connection Fix
# 泰坦陨落 2》服务器连接修复
------------------------------------------------------------------------------------------------------------------------------------------
中文：

##步骤：
1. 解压  `Titanfall2_Launcher.zip`。
2. 双击 `start_game_with_env.bat`批处理文件打开窗口。
3. 在窗口打开时，手动启动 Titanfall 2。（游玩 Titanfall 2时，请保持本程序窗口页面打开）
4. 不需要游戏联机时，关闭程序窗口以取消设置的环境变量。

如果没有安装 Python，请先安装 Python。

## 工作原理：
批处理文件会设置一个环境变量`OPENSSL_ia32cap`，以禁用会导致游戏兼容性问题的特定 CPU 功能。Python 脚本只需打开一个窗口，使环境变量保持激活状态。关闭窗口将取消设置变量。

## 文件：
- `start_game_with_env.bat` - 设置环境变量并启动 Python 脚本。
- `set_env_var.py` - 打开一个窗口以保持环境变量处于活动状态。
- `README.md` - 该文件包含说明。

## 要求
- 系统已安装 Python。
-------------------------------------------------------------------------------------------------------------------------------------------
ENGLISH:

##Steps:
1. Extract `Titanfall2_Launcher.zip`.
2. Double-click the `start_game_with_env.bat` batch file to open the window.
3. While the window is open, manually start Titanfall 2. (Keep the program window open while playing Titanfall 2)
4. Close the program window to unset the environment variable.

If Python is not installed, please install Python first.

## How it works:
The batch file sets an environment variable `OPENSSL_ia32cap` to disable specific CPU features that cause compatibility issues with the game. The Python script simply holds a window open to keep the environment variable active. Closing the window will unset the variable.

## Files：
- `start_game_with_env.bat` - Sets the environment variable and starts the Python script.
- `set_env_var.py` - Opens a window to keep the environment variable active.
- `README.md` - This file with instructions.

## Requirements
- Python installed on your system.