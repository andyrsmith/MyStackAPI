import random
from typing import List, Dict, Optional
from app.db.session import CSVSession
from app.schemas.resource import Catalog, RandomPickResponse


def get_all_items(session: CSVSession) -> List[Catalog]:
    """Return all resources from the CSV."""
    return [Catalog(**row) for row in session.data]


def get_random_by_category(session: CSVSession) -> List[RandomPickResponse]:
    """Return one random resource per category."""
    categories: Dict[str, List[dict]] = {}

    for row in session.data:
        cat = row.get("category", "uncategorized").strip()
        categories.setdefault(cat, []).append(row)

    results = []
    for category, items in sorted(categories.items()):
        pick = random.choice(items)
        results.append(
            RandomPickResponse(category=category, catalog=Catalog(**pick))
        )

    return results
