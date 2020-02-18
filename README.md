# DC_Easy

### it's XOT branch!!! 

> ### 2/18 自訂權限
> - `owncheck` (自訂權限者檢查)
> - yaml：
> - ```yaml
>   bot:
>       owner: # 自訂權限擁有者(member ID)
>   ```
> - `ownadd` (增加自訂權限者) 和 `ownre` (移除自訂權限者)
> - ```py
>   did = discord.Member.id
>   yamlhook("config.yaml").owner(did,process="append")
>   # append : list 增加
>   # remove : 移除
>   ```
> - 錯誤處理方式：
> - ```py
>   error = "使用者沒有自訂權限/不在自訂權限名單內。"
>   # 因為process是自訂，錯誤訊息需自行撰寫。
>   await Errors.error_process(self,ctx,error,process="custom")
>   ```