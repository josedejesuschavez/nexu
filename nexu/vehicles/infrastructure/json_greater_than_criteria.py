from vehicles.domain.criteria import Criteria


class JSONGreaterThanCriteria(Criteria):
    def __init__(self, min_price: int):
        self.min_price = min_price

    def filter(self, buffer):
        return [item for item in buffer if item["average_price"] >= self.min_price]
