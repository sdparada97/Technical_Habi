# Core Library
from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_all_with_filters(self):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def create(self, item):
        raise NotImplementedError

    @abstractmethod
    def update(self, item):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError
