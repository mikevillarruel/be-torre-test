from app.domain.services import TorreService
from app.infrastructure.repositories import TorreRepository


def get_torre_repository():
    return TorreRepository()


def get_torre_service():
    return TorreService(repository=get_torre_repository())
