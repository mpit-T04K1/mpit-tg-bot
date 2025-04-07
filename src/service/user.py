
from sqlalchemy import insert, update, select
from sqlalchemy.orm import Session

from src.database.models import UserORM
from src.schemas import UserSchema, UserModifySchema

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def exist(self, id: int) -> bool:
        stmt = (
            select(UserORM)
            .where(UserORM.id == id)
        )
        res = self.session.execute(stmt)
        res = res.scalar_one_or_none()
        return bool(res)


    def add(self, user_data: UserSchema) -> None:
        stmt = (
            insert(UserORM)
            .values(**user_data.model_dump(exclude_none=True))
        )
        self.session.execute(stmt)
        self.session.commit()

    def edit(self, user_data: UserModifySchema) -> None:
        stmt = (
            update(UserORM)
            .values(**user_data.model_dump(exclude_none=True))
            .filter_by(id=user_data.id)
        )
        self.session.execute(stmt)
        self.session.commit()


    
    def get_list(self) -> list[UserSchema]:
        stmt = select(UserORM)
        res = self.session.execute(stmt)
        res = res.scalars()
        return [UserSchema(**user_record.__dict__) for user_record in res]

