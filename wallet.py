import re
from typing import List, Optional

import click

from base import BaseWallet
from exceptions import CategoryError, DateError, SumError


class Wallet(BaseWallet):
    """Класс для работы с электронным кошельком."""

    def __init__(self, file_name: str):
        self.__file_name = file_name

    @property
    def file_name(self):
        """file_name getter property."""
        return self.__file_name

    @file_name.setter
    def value(self, file_name: str):
        """file_name setter property."""
        self.__file_name = file_name

    def get_balance(self) -> None:
        """Метод для отображения баланса, расхода и дохода."""
        consumption: float = 0
        income: float = 0
        with open(self.__file_name, "r", encoding="utf-8") as file:
            for line in file:
                new_line: List[str] = line.split(",")
                if new_line[1] == "Расход":
                    consumption += float(new_line[2])
                else:
                    income += float(new_line[2])
        click.echo(
            f"[INFO] Баланс: {income - consumption}\n"
            f"[INFO] Расход: {consumption}\n"
            f"[INFO] Доход: {income}\n"
        )

    def add_record(
            self,
            date: str,
            category: str,
            summa: float,
            description: str,
    ) -> None:
        """Метод для добавления информации о расходах и доходах."""
        category = category.title()
        self.is_valid(date, summa, category)
        with open(self.__file_name, "a", encoding="utf-8") as file:
            file.write(f"{date},{category},{summa},{description}\n")

    def search_record(
            self,
            date: Optional[str],
            category: Optional[str],
            summa: Optional[float],
    ) -> None:
        """
        Метод для поиска записей о расходах и доходах по дате,
        категории, сумме.
        """
        if not any((date, category, summa)):
            click.echo("[ERROR] Данные не были переданы.")
            return
        self.is_valid(date, summa, category)
        with open(self.__file_name, "r", encoding="utf-8") as file:
            for index, line in enumerate(file):
                new_line: List[str] = line.split(",")
                if date:
                    if new_line[0] == date:
                        click.echo(f'[INFO] id:{index} -> {line.rstrip()}')
                elif category:
                    if new_line[1] == category.title():
                        click.echo(f'[INFO] id:{index} -> {line.rstrip()}')
                elif summa:
                    if float(new_line[2]) == summa:
                        click.echo(f'[INFO] id:{index} -> {line.rstrip()}')

    def edit_record(
            self,
            id: Optional[int],
            date: Optional[str],
            category: Optional[str],
            summa: Optional[float],
            description: Optional[str],
    ) -> None:
        """Метод для изменения записи о расходах и доходах."""
        category = category.title() if category else None
        self.is_valid(date, summa, category)
        with open(self.__file_name, "r", encoding="utf-8") as file:
            record_list: List[str] = file.readlines()
            record: List[str] = record_list.pop(id).split(",")
            record[0] = date if date else record[0]
            record[1] = category if category else record[1]
            record[2] = str(summa) if summa else record[2]
            record[3] = description if description else record[3]
            record_list.insert(id, ",".join(record) + "\n")
        with open(self.__file_name, "w", encoding="utf-8")as file:
            file.write("".join(record_list))

    def all_record(self) -> None:
        """Метод для вывода все записей о расходах и доходах."""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            for index, line in enumerate(file):
                click.echo(f"[INFO] id:{index} -> {line.rstrip()}")

    def validate_date(self, value: Optional[str]) -> None:
        """Метод для проверки формата даты."""
        if value:
            reg = re.compile(
                r"(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d"
            )
            if not reg.match(value):
                raise DateError()

    def validate_sum(self, value: Optional[float]) -> None:
        """Метод для проверки суммы."""
        if value and value < 0:
            raise SumError()

    def validate_category(self, value: Optional[str]) -> None:
        """Метод для проверки категории."""
        if value and value not in ("Расход", "Доход"):
            raise CategoryError()

    def is_valid(self, data: str, summa: float, category: str) -> None:
        """Общий метод валидации."""
        if data:
            self.validate_date(data)
        elif summa:
            self.validate_sum(summa)
        elif category:
            self.validate_category(category)
