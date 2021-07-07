from fastapi import APIRouter

from routes.company import company_router

router = APIRouter()

router.include_router(company_router, prefix="/company")
