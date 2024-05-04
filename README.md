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
- Изменение записей о доходах и расходах. Что бы изменить запись нужно получить id записи командой **python my_wallet.py all-record**
  - Windows
  ```
  python my_wallet.py edit-record --help
  python my_wallet.py edit-record
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py edit-record --help
  python3 my_wallet.py edit-record
  ```
- Поиск записей по дате, категории и сумме:
  - Windows
  ```
  python my_wallet.py search-record --help
  python my_wallet.py search-record
  ```
  - Linux/macOS
  ```
  python3 my_wallet.py search-record --help
  python3 my_wallet.py search-record
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
