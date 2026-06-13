import random
from typing import List, Dict, Optional
from app.db.session import CSVSession
from app.schemas.resource import Resource, RandomPickResponse


def get_all_resources(session: CSVSession) -> List[Resource]:
    """Return all resources from the CSV."""
    return [Resource(**row) for row in session.data]


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
            RandomPickResponse(category=category, resource=Resource(**pick))
        )

    return results
