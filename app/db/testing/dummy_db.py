from types import SimpleNamespace
from app.db import models

class DummyQuery:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def filter(self, *args, **kwargs):
        # Only supports filter by attribute equality for demo purposes
        results = self.data
        for arg in args:
            if hasattr(arg, 'left') and hasattr(arg, 'right'):
                key = arg.left.name
                value = arg.right.value
                results = [item for item in results if getattr(item, key) == value]
        for k, v in kwargs.items():
            results = [item for item in results if getattr(item, k) == v]
        return DummyQuery(self.model, results)

    def filter_by(self, **kwargs):
        results = self.data
        for k, v in kwargs.items():
            results = [item for item in results if getattr(item, k) == v]
        return DummyQuery(self.model, results)

    def all(self):
        return self.data

    def first(self):
        return self.data[0] if self.data else None

    def in_(self, values):
        # Used for .in_ queries
        return [item for item in self.data if getattr(item, 'id', None) in values]

class DummySession:
    def __init__(self):
        # Hardcoded dummy data for demonstration
        self._users = [
            SimpleNamespace(id=1, email="test@example.com", first_name="Test", last_name="User")
        ]
        self._purchases = [
            SimpleNamespace(id=1, user_id=1, cat_id=1, video_id=None),
            SimpleNamespace(id=2, user_id=1, cat_id=None, video_id=2)
        ]
        self._live_events = [
            SimpleNamespace(id=2, name="Sample Video", location="Test Location", start="2024-01-01T10:00:00Z", end="2024-01-01T12:00:00Z", timezone="UTC", embed2="mux123", category=1),
            SimpleNamespace(id=3, name="Another Video", location="Another Location", start="2024-01-02T10:00:00Z", end="2024-01-02T12:00:00Z", timezone="UTC", embed2="mux456", category=2)
        ]

    def query(self, model):
        if model == models.User:
            return DummyQuery(models.User, self._users)
        if model == models.Purchase:
            return DummyQuery(models.Purchase, self._purchases)
        if model == models.LiveEvent:
            return DummyQuery(models.LiveEvent, self._live_events)
        return DummyQuery(model, [])

    def close(self):
        pass

def get_dummy_db():
    db = DummySession()
    try:
        yield db
    finally:
        db.close()
