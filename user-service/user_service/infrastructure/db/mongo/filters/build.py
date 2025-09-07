from user_service.infrastructure.db.mongo.filters.base import BaseFilters


def build_mongo_filters(filters: object, filters_impl: type[BaseFilters]) -> dict:
    _filters = {}
    for key, value in filters.__dict__.items():
        if type(value) is bool or value:
            _filters.update(filters_impl().__dict__[key](value))
    return _filters
