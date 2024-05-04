import click

from constants import FILE_NAME
from exceptions import CategoryError, DateError, SumError
from wallet import Wallet

wallet = Wallet(FILE_NAME)


@click.group()
def my_balance():
    """Группа команд для управления кошельком."""
    pass


@click.command()
def get_balance() -> None:
    """Команда для отображения текущего баланса, расходов и доходов."""
    wallet.get_balance()


@click.command()
@click.option("-d", "--date", prompt="Дата", help="Текущая дата.")
@click.option(
    "-c",
    "--category",
    prompt="Категория",
    help="Категория в формате Расход/Доход.",
)
@click.option("-s", "--sum", type=click.FLOAT, prompt="Сумма", help="Сумма.")
@click.option(
    "-desc",
    "--description",
    prompt="Описание",
    help="Описание.",
)
def add_record(date: str, category: str, sum: float, description: str) -> None:
    """Команда для добавление записи о доходах или расходах."""
    wallet.add_record(date, category, sum, description)


@click.command()
@click.option("-id", "--id", type=click.INT, default=None, help="id.")
@click.option("-d", "--date", default=None, help="Дата.")
@click.option("-c", "--category", default=None, help="Категория.")
@click.option("-s", "--sum", type=click.FLOAT, default=None, help="Сумма.")
@click.option(
    "-desc",
    "--description",
    default=None,
    help="Описание.",
)
def edit_record(
    id: int, date: str, category: str, sum: float, description: str
) -> None:
    """Команда для изменения записи о доходах или расходах."""
    wallet.edit_record(id, date, category, sum, description)


@click.command()
@click.option("-d", "--date", default=None, help="По дате.")
@click.option("-c", "--category", default=None, help="По категории.")
@click.option("-s", "--sum", type=click.FLOAT, default=None, help="По сумме.")
def search_record(date: str, category: str, sum: float) -> None:
    """Команда для поиска записи по дате, категории, сумме."""
    wallet.search_record(date, category, sum)


@click.command()
def all_record():
    """Команда для отображения всех записей."""
    wallet.all_record()


my_balance.add_command(get_balance)
my_balance.add_command(add_record)
my_balance.add_command(edit_record)
my_balance.add_command(search_record)
my_balance.add_command(all_record)

if __name__ == "__main__":
    try:
        my_balance()
    except FileNotFoundError:
        click.echo("[ERROR] Вы еще не добавили записи.")
    except CategoryError:
        click.echo("[ERROR] Категория должна быть в формате Расход/Доход.")
    except DateError:
        click.echo("[ERROR] Формат даты должен быть DD.MM.GGGG.")
    except SumError:
        click.echo("[ERROR] Сумма не может быть отрицательной.")
