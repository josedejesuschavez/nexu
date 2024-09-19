from vehicles.domain.criteria import Criteria


class JSONLessThanCriteria(Criteria):
    def __init__(self, max_price: int):
        self.max_price = max_price

    def filter(self, buffer):
        return [item for item in buffer if item['average_price'] <= self.max_price]
