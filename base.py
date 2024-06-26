from abc import ABC, abstractmethod
from typing import Optional


class BaseWallet(ABC):
    """Базовый класс для класса Wallet"""

    @abstractmethod
    def get_balance(self) -> None:
        pass

    @abstractmethod
    def add_record(
            self,
            date: str,
            category: str,
            summa: float,
            description: str,
    ) -> None:
        pass

    @abstractmethod
    def search_record(
            self,
            date: Optional[str],
            category: Optional[str],
            summa: Optional[float],
    ) -> None:
        pass

    @abstractmethod
    def edit_record(
            self,
            id: Optional[int],
            date: Optional[str],
            category: Optional[str],
            summa: Optional[float],
            description: Optional[str],
    ) -> None:
        pass
