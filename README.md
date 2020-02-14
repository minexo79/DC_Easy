# DC_Easy

[![python-version](https://img.shields.io/pypi/pyversions/discord.py?style=flat)](https://www.python.org/)
[![commit](https://img.shields.io/github/last-commit/minexo79/dc_base_bot)](https://github.com/minexo79/dc_base_bot)
[![size](https://img.shields.io/github/repo-size/minexo79/DC_Easy?style=social)]
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
## 👾專案介紹 - Introduction
給初學者們方便開發，使用的discord機器人。 

---
## 👾開發夥伴 - Develop Team

|人員名稱|備註|
|:-----|:----|
|[XOT](https://github.com/minexo79)|程式開發&專案總召|
|[HTG-YT](https://github.com/HTG-YT)|程式開發|
|[ShibaInu](https://github.com/neo123440)|程式開發|

---
## 👾機器人架構 - Bot Architecture

### `cmds`：指令放置區
- `info.py`：提供資訊（關於機器人，查詢延遲）
- `owner.py`：核心管理功能（重新裝載Cog，關閉機器人）
- `manage.py`：一般管理功能（查詢人物，群組資訊）
- `event.py`：事件管理功能（偵測錯誤）
### `core`：核心模組區
- `classes.py`：Cog核心
- `datahook.py`：資料勾手（更方便的讀取資料等...）`（註一）`
- `errors.py`：錯誤處理（一般方式，自訂方式處理）`（註二）`

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

> ### (註二) error使用範例：
> ```py
> from core.errors import Errors
> 
> async def on_command_error(self, ctx, error): # 出現指令錯誤
>   await Errors.error_process(self,ctx,error,process="default") # 呼叫錯誤處理器
>   # 一般方式處理： process = "default"
>   # 自訂方式處理： process = "custom"
> ```
