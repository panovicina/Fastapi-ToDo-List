from fastapi import APIRouter

from app.routers.v1.lists import router as list_router
from app.routers.v1.tasks import router as task_router
from app.routers.v1.users import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(user_router)
router.include_router(task_router)
router.include_router(list_router)
