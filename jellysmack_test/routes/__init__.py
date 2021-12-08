from fastapi import APIRouter

from .character_router import router as character_router
from .episode_router import router as episode_router
from .comment_router import router as comment_router

main_router = APIRouter()
main_router.include_router(character_router, prefix="/character", tags=["character"])
main_router.include_router(episode_router, prefix="/episode", tags=["episode"])
main_router.include_router(comment_router, prefix="/comment", tags=["comment"])
