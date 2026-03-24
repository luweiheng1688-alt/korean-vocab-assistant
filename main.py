import webview
import os
import sys

# 彻底锁死路径：无论你怎么运行、怎么打包，存档永远和软件保存在同一个文件夹！
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(base_dir, 'korean_data.json')
HTML_FILE = os.path.join(base_dir, 'index.html')

class Api:
    def save_data(self, data_str):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            f.write(data_str)
        return "ok"

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

if __name__ == '__main__':
    api = Api()
    # 注入 API 并启动软件
    window = webview.create_window('每日韩语', HTML_FILE, js_api=api, width=450, height=800)
    webview.start(http_server=True)