import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from starlette.testclient import TestClient

from jellysmack_test.db import Base, get_session
from jellysmack_test.app import app

TestingSession = scoped_session(sessionmaker())


def pytest_runtestloop(session):
    """
    Hook called before the main runtest loop.
    """
    engine = engine = create_engine("sqlite:///./test.db")
    TestingSession.configure(bind=engine)
    Base.metadata.create_all(engine)


def pytest_sessionfinish(session, exitstatus):
    """
    Hook called after whole test run finished.
    Delete the test db.
    """
    import os

    if os.path.isfile("test.db"):
        os.remove("test.db")


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """Executed before each test"""
        # Prepare a new, clean session
        self.session = TestingSession()

    def tearDown(self):
        """Executed after each test"""

        # Delete changes to the database
        for table in reversed(Base.metadata.sorted_tables):
            # print(f"Clear table {table}")
            self.session.execute(table.delete())
        self.session.commit()

        # Remove it, so that the next test gets a new Session()
        TestingSession.remove()


class BaseApiTestCase(BaseTestCase):
    def override_get_session(self):
        """Override get_session for testing"""
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    def setUp(self):
        """Executed before each test"""
        super().setUp()
        app.dependency_overrides[get_session] = self.override_get_session
        self.client = TestClient(app)
