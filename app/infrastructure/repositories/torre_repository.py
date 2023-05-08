import http.client
import json

from app.domain.interfaces import ITorreRepository
from app.domain.models import User, Skill, Experience, UserSkillDetails


class TorreRepository(ITorreRepository):
    def get_user_by_username(self, username: str) -> User:
        conn = http.client.HTTPSConnection("bio.torre.co")
        conn.request("GET", f"/api/bios/{username}")
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        person = data['person']

        skills: list[Skill] = []

        for strength in data['strengths']:
            skill: Skill = Skill(
                id=strength['id'],
                name=strength['name'],
                proficiency=strength['proficiency'],
                recommendations=strength['recommendations'],
                weight=strength['weight']
            )
            skills.append(skill)

        return User(
            id=person['id'],
            username=username,
            name=person['name'],
            skills=skills,
            picture=person.get('picture'),
            professional_headline=person.get('professionalHeadline'),
            verified=person['verified'],
        )

    def get_user_skill_details(self, username: str, skill_id: str) -> UserSkillDetails:
        conn = http.client.HTTPSConnection("torre.co")
        conn.request("GET", f"/api/genome/bios/{username}/strengths-skills/{skill_id}/detail")
        res = conn.getresponse()
        data = res.read()
        response = json.loads(data)
        related_experiences = response['relatedExperiences']
        experiences: list[Experience] = []

        skill = Skill(
            id=response['id'],
            name=response['name'],
            proficiency=response['stats']['proficiency'],
            recommendations=response['stats']['recommendations'],
            weight=response['weight']
        )

        if related_experiences:
            for related_experience in related_experiences:
                experience = Experience(
                    id=related_experience['id'],
                    name=related_experience['name'],
                    organization=related_experience['organizations'][0]['name'],
                    from_year=related_experience.get('from_year'),
                    from_month=related_experience.get('from_month'),
                    to_year=related_experience.get('to_year'),
                    to_month=related_experience.get('to_month')
                )
                experiences.append(experience)

        return UserSkillDetails(skill=skill, experiences=experiences)

    def get_users_skilled_in(self, skill_name: str, skill_proficiency: str, size: int) -> list[User]:
        payload = json.dumps({
            "and": [
                {
                    "skill/role": {
                        "text": skill_name,
                        "proficiency": skill_proficiency,
                    }
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json',
        }
        conn = http.client.HTTPSConnection("search.torre.co")
        conn.request("POST", f"/people/_search?size={size}", body=payload, headers=headers)
        res = conn.getresponse()
        data = res.read()
        response = json.loads(data)
        results = response.get('results')
        users: list[User] = []

        if results:
            for item in results:
                user = User(
                    username=item['username'],
                    name=item['name'],
                    picture=item.get('picture'),
                    professional_headline=item.get('professionalHeadline'),
                    verified=item['verified'],
                )
                users.append(user)

        return users
