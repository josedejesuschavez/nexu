from vehicles.domain.criteria import Criteria


class SQLGreaterThanCriteria(Criteria):
    def __init__(self, min_price: int):
        self.min_price = min_price

    def filter(self, buffer):
        return buffer.filter(average_price__gte=self.min_price)
