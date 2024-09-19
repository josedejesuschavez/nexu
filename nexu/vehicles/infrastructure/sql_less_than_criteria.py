from vehicles.domain.criteria import Criteria


class SQLLessThanCriteria(Criteria):
    def __init__(self, max_price: int):
        self.max_price = max_price

    def filter(self, buffer):
        return buffer.filter(average_price__lte=self.max_price)
