def build_mongo_filters(filters: object) -> dict:
    _filters = {}
    for key, value in filters.__dict__.items():
        if value is not None:
            _filters[key] = value
    return _filters
