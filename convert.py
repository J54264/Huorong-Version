import requests
import re
from datetime import datetime

def fetch_data():
    url = "https://www.huorong.cn/versionShow.php"
    response = requests.get(url)
    return response.json()

def update_readme(data):
    # 生成新版本文档块
    new_content = f"""
<!-- HUORONG_VERSION_START -->
## 🛡️ 火绒安全软件实时版本信息 (自动更新)
**最后更新时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

| 属性        | 值                          |
|-------------|-----------------------------|
| 病毒库版本  | `{data['virusVersion']}`    |
| 程序版本    | `{data['version']}`         |
| 生成时间    | `{data['createtime']}`      |

### 下载链接
- **x86/x64 完整包**: [{data['fullName']}]({data['urlFull']}) ({data['filesize']})
- **ARM64 完整包**: [{data['armFullName']}]({data['armUrlFull']}) ({data['armFilesize']})
<!-- HUORONG_VERSION_END -->"""

    # 读取并替换 README
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    # 使用正则表达式精准替换标记之间的内容
    updated_content = re.sub(
        r'<!-- HUORONG_VERSION_START -->.*?<!-- HUORONG_VERSION_END -->',
        new_content,
        readme_content,
        flags=re.DOTALL  # 允许匹配多行
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    try:
        data = fetch_data()
        update_readme(data)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
