from user_service.infrastructure.db.mongo.filters.base import BaseFilters


class UserFiltersMongo(BaseFilters):
    def __init__(self) -> None:
        self.username = lambda v: {'username': v}
        self.username_ilike = lambda v: {'username': {'$regex': v}}
