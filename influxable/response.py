class InfluxDBResponse:
    def __init__(self, raw_json):
        self._raw_json = raw_json

    @property
    def raw(self):
        return self._raw_json

    @property
    def series(self):
        if 'results' in self.raw:
            results = self.raw['results']
            if len(results):
                result = results[0]
                if 'series' in result:
                    return [InfluxDBResponseSerie(s) for s in result['series']]
        return []


class InfluxDBResponseSerie:
    def __init__(self, json_serie):
        self._raw_json_serie = json_serie

    @property
    def raw(self):
        return self._raw_json_serie

    @property
    def columns(self):
        return self._raw_json_serie["columns"]

    @property
    def name(self):
        return self._raw_json_serie.get("name", "default")

    @property
    def values(self):
        return self._raw_json_serie["values"]
