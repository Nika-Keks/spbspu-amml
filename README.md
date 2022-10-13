# spbstu-amml

Пакет для хранения данных и моделей и быстрого их использования

---
## Модуль spbstuamml

Для загрузки одной из поддерживаемых моделей необходимо установить пакет `spbstu-amml`

```console
$ pip install spbstu-amml 
```

Пример получения модели:

```python
from spbstuamml.models import vgg
model = vgg.vgg16_from_hub(dataset="pneumonia")
print(model.layers[:4])
```
```bash
[<keras.engine.functional.Functional object at 0x7f736e8e2d70>, <keras.layers.reshaping.flatten.Flatten object at 0x7f736dea3130>, <keras.layers.core.dense.Dense object at 0x7f736dec9bd0>]
```

Модель будет загружена и прочитана из файла.

Внимание! 
Пакет не тянет за собой библиотеки для машинного обучения, их пользователь должен установитьс сам.

---
## datahub

Утилита для настройки доступа к удаленному хнанилищу

```console
$ python3 -m datahub -h

Datahub utils to manage the data repository configuration

positional arguments:
  {configure}  utils command

options:
  -h, --help   show this help message and exit
```

Для ввода ключей доступа и региона енобходимо выполнить соманду `configure` и ввести параметры:

```console
$ python3 -m datahub configure
Enter Access Key ID:access-key-id
Enter Secret Access key:secret-access-key
Enter Region:default
```

или ввести парапетры в качестве аргументов команды:

```console
$ python3 -m datahub configure \
> --access-key-id "access-key-id" \
> --secret-access-key "secret-access-key" \
> --region "default"
```