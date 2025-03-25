import requests
import json
from datetime import datetime

def fetch_data():
    url = "https://www.huorong.cn/versionShow.php"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data")

def generate_markdown(data):
    markdown = f"""## 火绒安全软件版本信息 (自动更新)
**最后更新时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

### 基础信息
- **病毒库版本**: `{data['virusVersion']}`
- **程序版本**: `{data['version']}`
- **生成时间**: `{data['createtime']}`

### 常规版本 (x86/x64)
| 类型       | 文件名                                      | 大小    | 下载链接                                   |
|------------|--------------------------------------------|---------|--------------------------------------------|
| 完整安装包 | `{data['fullName']}` | {data['filesize']} | [下载]({data['urlFull']}) |
| 全功能安装包 | `{data['allName']}` | {data['filesize']} | [下载]({data['urlAll']}) |

### ARM64 版本
| 类型       | 文件名                                      | 大小    | 下载链接                                   |
|------------|--------------------------------------------|---------|--------------------------------------------|
| 完整安装包 | `{data['armFullName']}` | {data['armFilesize']} | [下载]({data['armUrlFull']}) |
| 全功能安装包 | `{data['armAllName']}` | {data['armFilesize']} | [下载]({data['armUrlAll']}) |
"""
    return markdown

if __name__ == "__main__":
    data = fetch_data()
    md_content = generate_markdown(data)
    with open("VERSION.md", "w", encoding="utf-8") as f:
        f.write(md_content)
