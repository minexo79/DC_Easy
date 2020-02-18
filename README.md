# DC_Easy

### it's XOT branch!!! 

> ### 2/18 自訂權限
> - `owncheck` (自訂權限檢查)
> - yaml：
> - ```yaml
>   bot:
>       owner: # 自訂權限擁有者(member ID)
>   ```
> - 錯誤處理方式：
> - ```py
>   error = "使用者沒有自訂權限/不在自訂權限名單內。"
>   # 因為process是自訂，錯誤訊息需自行撰寫。
>   await Errors.error_process(self,ctx,error,process="custom")
>   ```
