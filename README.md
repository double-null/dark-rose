# Dark Rose Clicker

### Запуск

1. Перед запуском в "белочке" отключить подсказки адресной строки.

```sh
Настройки > Адресная Панель > Включить автозаполнение
```
2. Убедиться, что кодировка стоит английская. (Баг Windows с потерей символов)

3. Установить разрешение экрана 1920 x 1080

4. Отредактировать файл config.ini

5. Заполнить accounts.txt аккаунтами по маске:

```
{login}:{password}:{server1}.{server2}.{serverN}
```
Пример:

```
test@provider.loc:password:77.78.99.100
```

6. Открыть страницу с логином

### Команды для кастомного скрипта:

<b>click {x} {y}</b> - клик по координатам x, y

<b>double {x} {y}</b> - двойной клик по координатам x, y

<b>write {text}</b> - вставка текста

<b>image {pict.png}</b> - клик по изображению (изображения хранить в директории images)

<b>wait {x}</b> - задержка на заданное количество секунд

### Примечания:

Компиляция под Windows:
```sh
$ auto-py-to-exe
```