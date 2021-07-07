from fastapi import APIRouter
from routes.company import companyR


router = APIRouter()

router.include_router(companyR, prefix="/company")

