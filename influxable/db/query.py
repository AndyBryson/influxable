from functools import lru_cache
from .. import Influxable


class RawQuery:
    def __init__(self, str_query):
        self.str_query = str_query

    def execute(self):
        return self.raw_response

    @property
    def raw_response(self):
        return self._resolve()

    @lru_cache(maxsize=None)
    def _resolve(self, *args, **kwargs):
        instance = Influxable.get_instance()
        return instance.execute_query(query=self.str_query, method='post')


class Query(RawQuery):
    def __init__(self):
        self.initial_query = '{select_clause} {from_clause} LIMIT 5'
        self.from_clause = 'FROM {measurements}'
        self.select_clause = 'SELECT {fields}'
        self.selected_fields = '*'

    def from_measurements(self, *measurements):
        self.selected_measurements = ', '.join(measurements)
        return self
