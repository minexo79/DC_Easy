# DC_Easy

[![python-version](https://img.shields.io/pypi/pyversions/discord.py?style=flat)](https://www.python.org/)
[![discord.py](https://img.shields.io/pypi/v/discord.py)](https://pypi.org/project/discord.py/)
[![commit](https://img.shields.io/github/last-commit/minexo79/DC_Easy)](https://github.com/minexo79/DC_Easy)
[![size](https://img.shields.io/github/repo-size/minexo79/DC_Easy?style=social)](https://github.com/minexo79/DC_Easy)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
## 👾專案介紹 - Introduction
[![DC_easy](./img/logo.png)](https://github.com/minexo79/DC_Easy)  
給初學者們方便開發，使用的discord機器人。 

---
## 👾開發夥伴 - Develop Team

|人員名稱|備註|
|:-----|:----|
|[XOT](https://github.com/minexo79)|程式開發&專案總召|
|[HTG-YT](https://github.com/HTG-YT)|程式開發|
|[ShibaInu](https://github.com/neo123440)|程式開發|

---
## 👾使用教學 - Tutorial

### 事前準備環境：

- 一般電腦，並且安裝了作業系統。
- python 3.6或更高。

### 建置步驟：
1. 將整個`git`下載並存放到任一目錄。
2. 將`config_example.yaml`改名成`config.yaml`並且裡面的`token: `填入bot所需要的Token碼。
3. 打開`powershell.exe`，進入到你的機器人存放目錄。
4. 輸入`pip install requirements.txt`，並等待安裝完畢。
5. 輸入`python bot.py`即可運行。

---
## 👾機器人架構 - Bot Architecture

### `cmds`：指令放置區
- `info.py`：提供資訊（關於機器人，查詢延遲，使用者及伺服器資訊查詢）
- `owner.py`：核心管理功能（Cog載入，移除，重裝，關閉機器人）
- `manage.py`：自訂權限管理功能（自定權限查詢，增加，移除）
- `event.py`：事件管理功能（偵測錯誤）
### `core`：核心模組區
- `classes.py`：Cog核心
- `datahook.py`：資料勾手（讀取yaml檔案）`（註一）`
- `errors.py`：錯誤處理（一般方式，自訂方式處理）`（註二）`


---
## 👾備註 - Note

> ### (註一) datahook使用範例：
> ```py
> from core.datahook import yamlhook
> 
> p = datahook("config.yaml") # 指定檔案
> p.load() # 開啟檔案 (唯讀模式)
> 
> print(p['bot']['token']) # 印出資料
> ```

> ### (註二) error使用範例：
> ```py
> from core.errors import error_process
> 
> async def on_command_error(self, ctx, error): # 出現指令錯誤
>   await error_process(ctx,error,process="default") # 呼叫錯誤處理器
>   # 一般方式處理： process = "default"
>   # 自訂方式處理： process = "custom"
>   # process指定custom，錯誤原因需要自己撰寫：
>   error = "自訂錯誤原因"。
>   await error_process(ctx,error,process="custom") # 呼叫錯誤處理器
> ```