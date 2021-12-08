from typing import List, Optional, TypeVar, Type
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session


class AssociativeModel:
    pass


# Create a generic variable that can be 'Model', or any subclass.
# See: https://stackoverflow.com/questions/44640479/mypy-annotation-for-classmethod-returning-instance
T = TypeVar("T", bound="Model")


class Model:
    """Custom Base Class for defining common methods or attributes."""

    id = Column(Integer, primary_key=True, index=True, nullable=False)

    @classmethod
    def _get_generic_query(cls, session: Session, filters: dict = None):
        query = session.query(cls)
        if filters:
            for attr, value in iter(filters.items()):
                query = query.filter(getattr(cls, attr) == value)
        return query

    @classmethod
    def fetch_by_id(cls, session: Session, obj_id: int, filters: dict = None):
        query = cls._get_generic_query(session, filters)
        return query.filter(cls.id == obj_id).first()

    @classmethod
    def fetch_all(
        cls, session: Session, offset: int = 0, limit: int = 100, filters=None
    ):
        query = cls._get_generic_query(session, filters)
        return query.offset(offset).limit(limit).all()

    @classmethod
    def delete(cls, session: Session, obj_id: int, offset: int = 0, limit: int = 100):
        query = cls._get_generic_query(session)
        return query.filter(cls.id == obj_id).delete()

    @classmethod
    def _update(
        cls: Type[T], session: Session, obj_id: int, update: dict
    ) -> Optional[T]:
        query = cls._get_generic_query(session)
        query = query.filter(cls.id == obj_id).update(update)
        session.commit()
        if query:
            return cls.fetch_by_id(session, obj_id)

    @classmethod
    def _create(cls: Type[T], session: Session, instance: T) -> T:
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance
