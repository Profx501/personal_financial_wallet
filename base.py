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
            sum: float,
            description: str,
    ) -> None:
        pass

    @abstractmethod
    def search_record(
            self,
            date: Optional[str],
            category: Optional[str],
            sum: Optional[float],
    ) -> None:
        pass

    @abstractmethod
    def edit_record(
            self,
            id: Optional[str],
            date: Optional[str],
            category: Optional[str],
            sum: Optional[float],
            description: Optional[str],
    ) -> None:
        pass
