# Консольное приложение "Личный финансовый кошелек"

## Описание
Приложение для учета личных доходов и расходов.
Реализация через консоль (CLI).
- Основные возможности:
- Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
- Добавление записи: Возможность добавления новой записи о доходе или расходе.
- Редактирование записи: Изменение существующих записей о доходах и расходах.
- Поиск по записям: Поиск записей по категории, дате или сумме.


## Технологии
- Python
- Click

## Запуск проекта
Для запуска проекта выполните следующие шаги:
1. Склонируйте репозиторий personal_financial_wallet на свой компьютер.
2. Создайте виртуальное окружение:
   - Windows
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```
   - Linux/macOS
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Обновить PIP:
   - Windows
   ```bash
   python -m pip install --upgrade pip
   ```
   - Linux/macOS
   ```bash
   python3 -m pip install --upgrade pip
   ```
4. Установить зависимости из файла requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
## Функционал
- Чтобы посмотреть доступные команды:
  - Windows
  ```
  python my_wallet.py --help
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py --help
  ```
- Добавление записи о расходах и доходах:
  - Windows
  ```
  python my_wallet.py add-record --help
  python my_wallet.py add-record
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py add-record --help
  python3 my_wallet.py add-record
  ```
- Отображение всех записей:
  - Windows
  ```
  python my_wallet.py all-record
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py all-record
  ```
  - Вывод:
  ```
  [INFO] id:0 -> 01.02.2003,Расход,2000.0,Покупка в магазине
  [INFO] id:1 -> 02.03.2003,Доход,6000.0,ЗП
  [INFO] id:2 -> 03.03.2003,Доход,10000.0,Оплата счета.
  ```
- Изменение записей о доходах и расходах. Что бы изменить запись нужно получить id записи командой **python my_wallet.py all-record**
  - Windows
  ```
  python my_wallet.py edit-record --help
  python my_wallet.py edit-record -id     -d        (Изменить дату)
  python my_wallet.py edit-record -id     -с        (Изменить категорию)
  python my_wallet.py edit-record -id     -s        (Изменить сумму)
  python my_wallet.py edit-record -id     -desc   (Изменить описание)
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py edit-record --help
  python3 my_wallet.py edit-record -id     -d        (Изменить дату)
  python3 my_wallet.py edit-record -id     -с        (Изменить категорию)
  python3 my_wallet.py edit-record -id     -s        (Изменить сумму)
  python3 my_wallet.py edit-record -id     -desc   (Изменить описание)
  ```
- Поиск записей по дате, категории и сумме:
  - Windows
  ```
  python my_wallet.py search-record --help
  python my_wallet.py search-record -d     (по дате)
  python my_wallet.py search-record -с     (по категории)
  python my_wallet.py search-record -s     (по сумме)
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py search-record --help
  python3 my_wallet.py search-record
  python3 my_wallet.py search-record -d     (по дате)
  python3 my_wallet.py search-record -с     (по категории)
  python3 my_wallet.py search-record -s     (по сумме)
  ```

- Выводит текущий баланс, расход и доход:
  - Windows
  ```
  python my_wallet.py get-balance
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py get-balance
  ```
  - Вывод:
  ```
  [INFO] Баланс: 14000.0
  [INFO] Расход: 2000.0
  [INFO] Доход: 16000.0
  ```

## Прочее
Файл с записями будет создан в директории с проектом. По умолчанию название файла personal_wallet.txt. Название файла можно поменять в файле constants.py.
