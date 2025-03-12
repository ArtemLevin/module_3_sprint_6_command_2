from abc import ABC, abstractmethod

class BaseTokenService(ABC):
    @abstractmethod
    def save_token(self, user_id: str, token: str, token_type: str, expires_in: int):
        pass

    @abstractmethod
    def get_token(self, user_id: str, token_type: str) -> str:
        pass

    @abstractmethod
    def delete_token(self, user_id: str, token_type: str):
        pass

    @abstractmethod
    def is_token_valid(self, user_id: str, token: str, token_type: str) -> bool:
        pass