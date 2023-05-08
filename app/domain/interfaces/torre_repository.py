from abc import ABC, abstractmethod

from app.domain.models import User, UserSkillDetails


class ITorreRepository(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> User | None:
        pass

    @abstractmethod
    def get_user_skill_details(self, username: str, skill_id: str) -> UserSkillDetails:
        pass

    @abstractmethod
    def get_users_skilled_in(self, skill_name: str, skill_proficiency: str, size: int) -> list[User]:
        pass
