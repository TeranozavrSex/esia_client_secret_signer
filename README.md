# Esia_client_secret_signer
Python3.11

API для шифрования client_secret для Госуслуг.

Подписывает данные с использованием ГОСТ Р 34.10-2012.

В файле укажите:
  1. **thumbprint** -> SHA1 отпечаток сертификата, связанного с закрытым ключем.
  2. Если нужно укажите другой путь до cryptcp

Был написан для Wundows Server 2019 запускается как сервис с помощью nssm.

На момент написания актуальная документация и полезные ссылки тут:
  - https://digital.gov.ru/ru/documents/6186/
  - https://github.com/sokolovs/esia-oauth2/blob/master/esia/utils.py
  - https://dev.rutoken.ru/pages/viewpage.action?pageId=65142840
  - https://estp.ru/test_eds/cert_install_linux
  - https://dev.rutoken.ru/pages/viewpage.action?pageId=72450199
  - https://oxylabs.io/blog/python-script-service-guide
  - https://www.cryptopro.ru/forum2/default.aspx?g=posts&t=6053

## Run server manual
```
  python esia_client_secret_signer.py
```

## Sign params
  Request url: **[server_url]**/sign/**[string-for-sign]**
