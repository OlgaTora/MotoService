from typing import Any
from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Any]:
        pass

    @abstractmethod
    async def get_by_id(self, id: Any) -> Any:
        pass

    @abstractmethod
    async def create(self, item: Any):
        pass

    @abstractmethod
    async def update(self, id: Any, item: Any):
        pass

    @abstractmethod
    async def delete(self, id: Any):
        pass
