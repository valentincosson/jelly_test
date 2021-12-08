from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session


class AssociativeModel:
    pass


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
    def fetch_by_id(cls, session: Session, id, filters: dict = None):
        query = cls._get_generic_query(session, filters)
        return query.filter(cls.id == id).first()

    @classmethod
    def fetch_all(
        cls, session: Session, offset: int = 0, limit: int = 100, filters=None
    ):
        query = cls._get_generic_query(session, filters)
        return query.offset(offset).limit(limit).all()
