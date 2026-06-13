import csv
from pathlib import Path
from typing import List
from app.schemas.resource import Resource


def _load_csv(path: str) -> List[dict]:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {path}")
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


class CSVSession:
    """Mimics a DB session but reads from a CSV file."""

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self._data: List[dict] = []

    def load(self):
        self._data = _load_csv(self.csv_path)

    @property
    def data(self) -> List[dict]:
        if not self._data:
            self.load()
        return self._data
