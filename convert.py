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
## 🛡️ 火绒安全软件5.0 实时版本信息 (自动更新)
**最后更新时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

### 核心信息
| 属性        | 值                          |
|-------------|-----------------------------|
| 病毒库版本  | `{data['virusVersion']}`    |
| 程序版本    | `{data['version']}`         |
| 生成时间    | `{data['createtime']}`      |

### 下载链接
#### x86/x64 架构
- **完整安装包**: [{data['fullName']} ({data['filesize']})]({data['urlFull']})
- **全功能安装包**: [{data['allName']} ({data['filesize']})]({data['urlAll']})

#### ARM64 架构
- **完整安装包**: [{data['armFullName']} ({data['armFilesize']})]({data['armUrlFull']})
- **全功能安装包**: [{data['armAllName']} ({data['armFilesize']})]({data['armUrlAll']})
<!-- HUORONG_VERSION_END -->"""

    # 读取原有 README
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    # 替换旧内容
    updated_readme = re.sub(
        r'<!-- HUORONG_VERSION_START -->.*?<!-- HUORONG_VERSION_END -->',
        new_content,
        readme,
        flags=re.DOTALL
    )

    # 写入新内容
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    data = fetch_data()
    update_readme(data)
