from abc import ABC, abstractmethod

class DatabaseInstance(ABC):
    @abstractmethod
    def get_db_connection(self):
        pass

    @abstractmethod
    def create(self, table: str, data: dict):
        pass

    @abstractmethod
    def read(self, table: str, conditions: dict = None):
        pass

    @abstractmethod
    def update(self, table: str, data: dict, conditions: dict = None):
        pass

    @abstractmethod
    def delete(self, table: str, conditions: dict):
        pass