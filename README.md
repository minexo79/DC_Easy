# dc_base_bot

[![python-version](https://img.shields.io/pypi/pyversions/discord.py?style=flat)](https://www.python.org/)
[![commit](https://img.shields.io/github/last-commit/minexo79/dc_base_bot)](https://github.com/minexo79/dc_base_bot)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
## 👾專案介紹 - Introduction
給初學者們方便開發，使用的discord機器人。 

---
## 👾開發夥伴 - Develop Team

|開發者|備註|
|:-----|:----|
|[XOT](https://github.com/minexo79)|程式開發&專案總召|
|[HTG-YT](https://github.com/HTG-YT)|程式開發|
|[ShibaInu](https://github.com/neo123440)|程式開發|

---
## 👾機器人架構 - Bot Architecture

### `cmds`：指令放置區
- `owner.py`：核心管理功能（重新裝載Cog，關閉機器人）
- `manage.py`：一般管理功能（查詢人物資料）
### `core`：核心模組區
- `classes.py`：Cog核心
- `datahook.py`：資料勾手（更方便的讀取資料等...）`（註一）`

---
## 👾備註 - Note

> ### (註一) datahook使用範例：
> ```py
> from core.datahook import yamlhook
> 
> p = datahook("config.yaml") # 指定檔案
> p.open() # 開啟檔案 (唯讀模式)
> 
> print(p['bot']['token']) # 印出資料
> ```
