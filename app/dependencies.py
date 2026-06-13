from app.db.session import CSVSession
from app.core.config import settings


def get_session() -> CSVSession:
    """Dependency that provides a loaded CSV session."""
    session = CSVSession(csv_path=settings.CSV_FILE_PATH)
    session.load()
    return session
