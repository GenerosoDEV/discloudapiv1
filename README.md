> ## Exemplos de uso

```{python}
import discloudapi

### STATUS DE UM BOT
resultado = discloud_api.BotStatus(bot_id=ID DO SEU BOT, api_token="SEU TOKEN DA DISCLOUD")
print(f"ID: {resultado.bot_id}\nUso de CPU: {resultado.cpu}\nUso de memória: {resultado.memory}")
print(f"{resultado.ratelimit_remaining}/{resultado.ratelimit}")

### SEU STATUS
resultado = discloud_api.UserStatus(api_token="SEU TOKEN DA DISCLOUD")
print(f"Seu plano: {resultado.plan}\nAcaba em: {resultado.planDataEnd}")
print(f"{resultado.ratelimit_remaining}/{resultado.ratelimit}")

### REINICIAR BOT
resultado = discloud_api.BotRestart(bot_id=ID DO SEU BOT, api_token="SEU TOKEN DA DISCLOUD")
print(f"{resultado.result}")
print(f"{resultado.ratelimit_remaining}/{resultado.ratelimit}")

### ACESSAR AS LOGS
resultado = discloud_api.BotRestart(bot_id=ID DO SEU BOT, api_token="SEU TOKEN DA DISCLOUD")
print(f"Logs completas: {resultado.link}\nÚltimos 1800 caracteres: {resultado.logs}")
print(f"{resultado.ratelimit_remaining}/{resultado.ratelimit}")
```
