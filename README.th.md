# A2A Python SDK 🐍

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
![PyPI - Version](https://img.shields.io/pypi/v/a2a-sdk)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/a2a-sdk)

<!-- markdownlint-disable no-inline-html -->

<html>
   <h2 align="center">
   <img src="https://raw.githubusercontent.com/google-a2a/A2A/refs/heads/main/docs/assets/a2a-logo-black.svg" width="256" alt="A2A Logo"/>
   </h2>
   <h3 align="center">ไลบรารี Python ที่ช่วยให้รันแอปพลิเคชัน Agentic ในรูปแบบ A2AServers ตาม <a href="https://google.github.io/A2A">Agent2Agent (A2A) Protocol</a> 🚀</h3>
</html>

<!-- markdownlint-enable no-inline-html -->

## การติดตั้ง 🛠️

คุณสามารถติดตั้ง A2A SDK โดยใช้ `uv` หรือ `pip`

## สิ่งที่ต้องมีก่อนติดตั้ง 📋

- Python 3.10+
- `uv` (ทางเลือก แต่แนะนำ) หรือ `pip`

### การใช้ `uv`

เมื่อคุณทำงานในโปรเจกต์ uv หรือสภาพแวดล้อมเสมือนที่จัดการโดย uv วิธีที่แนะนำในการเพิ่มแพ็คเกจคือการใช้ uv add

```bash
uv add a2a-sdk
```

### การใช้ `pip`

หากคุณต้องการใช้ pip ซึ่งเป็นตัวติดตั้งแพ็คเกจมาตรฐานของ Python คุณสามารถติดตั้ง `a2a-sdk` ได้ดังนี้

```bash
pip install a2a-sdk
```

## ตัวอย่างการใช้งาน 📝

### [ตัวอย่าง Helloworld](https://github.com/google-a2a/a2a-samples/tree/main/samples/python/agents/helloworld)

1. รัน Remote Agent

   ```bash
   git clone https://github.com/google-a2a/a2a-samples.git
   cd a2a-samples/samples/python/agents/helloworld
   uv run .
   ```

2. ในอีกเทอร์มินัลหนึ่ง รัน client

   ```bash
   cd a2a-samples/samples/python/agents/helloworld
   uv run test_client.py
   ```

คุณยังสามารถค้นหาตัวอย่าง Python เพิ่มเติมได้ [ที่นี่](https://github.com/google-a2a/a2a-samples/tree/main/samples/python) และตัวอย่าง JavaScript ได้ [ที่นี่](https://github.com/google-a2a/a2a-samples/tree/main/samples/js)

## ใบอนุญาต 📄

โปรเจกต์นี้ได้รับอนุญาตภายใต้เงื่อนไขของ [Apache 2.0 License](https://raw.githubusercontent.com/google-a2a/a2a-python/refs/heads/main/LICENSE)

## การมีส่วนร่วม 🤝

ดู [CONTRIBUTING.md](https://github.com/google-a2a/a2a-python/blob/main/CONTRIBUTING.md) สำหรับแนวทางการมีส่วนร่วม
