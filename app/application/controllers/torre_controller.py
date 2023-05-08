from fastapi import APIRouter, Depends, HTTPException

from app.di import get_torre_service
from app.domain.interfaces import ITorreService
from app.domain.models import User, UserSkillDetails

router = APIRouter()


@router.get("/{username}", response_model=User)
def get_user_by_username(username: str, service: ITorreService = Depends(get_torre_service)) -> User:
    user = service.get_user_by_username(username=username)
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.get("/{username}/{skill_id}", response_model=UserSkillDetails)
def get_user_skill_details(username: str, skill_id: str,
                           service: ITorreService = Depends(get_torre_service)) -> UserSkillDetails:
    return service.get_user_skill_details(username, skill_id)


@router.get("/{skill_name}/{skill_proficiency}/", response_model=list[User])
def get_users_skilled_in(skill_name: str, skill_proficiency: str, size: int = 2,
                         service: ITorreService = Depends(get_torre_service)) -> list[User]:
    return service.get_users_skilled_in(skill_name, skill_proficiency, size)
