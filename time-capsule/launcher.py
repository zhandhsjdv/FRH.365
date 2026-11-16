# -*- coding: utf-8 -*-
"""
时光胶囊启动器
--------------
只使用 Python 标准库：在本机开启一个临时网页服务，并自动用默认浏览器打开界面。
打包后用户双击 exe 即可使用，不需要安装 Python，也不需要联网。
关闭弹出的黑色命令行窗口即可退出程序。
"""

import functools
import http.server
import os
import socket
import socketserver
import sys
import threading
import urllib.parse
import webbrowser

HTML_NAME = "index.html"


def resource_dir() -> str:
    """打包后从临时解压目录读取资源；源码运行时用脚本所在目录。"""
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


def free_port() -> int:
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """不打印访问日志，保持控制台干净。"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=resource_dir(), **kwargs)

    def log_message(self, *args):
        pass


def main():
    if os.name == "nt":
        os.system("title 时光胶囊")

    html_path = os.path.join(resource_dir(), HTML_NAME)
    if not os.path.exists(html_path):
        print(f"错误：找不到界面文件 {html_path}")
        input("按回车键退出...")
        return

    port = free_port()
    url = f"http://127.0.0.1:{port}/{urllib.parse.quote(HTML_NAME)}"

    # 仅监听本机，外部电脑无法访问
    server = socketserver.ThreadingTCPServer(("127.0.0.1", port), QuietHandler)
    server.daemon_threads = True

    print("=" * 56)
    print("  时光胶囊已启动")
    print("  浏览器即将自动打开，如果没有弹出，请手动复制下面地址：")
    print("  " + url)
    print("  使用完毕后，直接关闭本窗口即可退出程序。")
    print("=" * 56)

    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
