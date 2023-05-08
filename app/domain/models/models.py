import pydantic


class Skill(pydantic.BaseModel):
    id: str
    name: str
    proficiency: str
    recommendations: int
    weight: float | None


class Experience(pydantic.BaseModel):
    id: str
    name: str
    organization: str
    from_year: str | None
    from_month: str | None
    to_year: str | None
    to_month: str | None


class User(pydantic.BaseModel):
    id: str | None
    username: str
    name: str
    skills: list[Skill] | None
    picture: str | None
    professional_headline: str | None
    verified: bool


class UserSkillDetails(pydantic.BaseModel):
    skill: Skill
    experiences: list[Experience]
