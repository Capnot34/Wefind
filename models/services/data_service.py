from typing import List

from data.users import User
from data.recruiter import Company
from data.resumes import Resume


def create_account(name: str, email: str, mobile: str, password: str, category: str, skills: list) -> User:
    user = User()

    user.name = name
    user.email = email
    user.mobile = mobile
    user.password = password
    user.category = category
    if skills:
        user.skills = skills

    user.save()
    return user


def create_company(name: str, email: str, location: str, industry: str, description: str) -> Company:
    company = Company()

    company.name = name
    company.email = email
    company.location = location
    company.industry = industry
    company.description = description

    company.save()
    return company


def create_resume(user, company, resume_content) -> Resume:
    resume = Resume(
        user=user,
        company=company,
        resume_content=resume_content
    )

    resume.save()
    return resume


def submit_resume(user_id, company_id, resume_file) -> Resume:
    user = User.objects.get(id=user_id)
    company = Company.objects.get(id=company_id)

    resume = Resume(
        user=user,
        company=company,
    )

    resume.resume_file.put(resume_file)
    resume.save()

    return resume


def find_user_my_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user


def find_company_by_email(email: str) -> Company:
    company = Company.objects(email=email).first()
    return company


def get_resume_by_company(company_id):
    return Resume.objects(company=company_id)
