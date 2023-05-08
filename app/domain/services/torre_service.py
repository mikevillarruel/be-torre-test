from app.domain.interfaces import ITorreService, ITorreRepository
from app.domain.models import User, UserSkillDetails


class TorreService(ITorreService):

    def __init__(self, repository: ITorreRepository):
        self.repository = repository

    def get_user_by_username(self, username: str) -> User:
        return self.repository.get_user_by_username(username)

    def get_user_skill_details(self, username: str, skill_id: str) -> UserSkillDetails:
        return self.repository.get_user_skill_details(username, skill_id)

    def get_people_skilled_in(self, skill_name: str, skill_proficiency: str, size: int) -> list[User]:
        return self.repository.get_people_skilled_in(skill_name, skill_proficiency, size)
