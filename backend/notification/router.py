from fastapi import APIRouter
from backend.models.db_model import Notification
from backend.database import db_dependency

notif_router = APIRouter(prefix='/notification')


@notif_router.post('/notif_save')
async def save_notif_to_db(db: db_dependency, msg: str):
    new_notif = Notification(
        message=msg
    )
    db.add(new_notif)
    await db.commit()
    await db.refresh(new_notif)
