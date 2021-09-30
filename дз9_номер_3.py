class Worker:
    def __init__(self, name, surname, wage, position, bonus):
        self.name = name
        self.surname = surname
        self._income={"profit": wage,"bonus":bonus}
    class position (worker):
        def get_full_name (self):
            return f"{self.name} {self.surname}"
        def get_total_income (self):
            return f"{sun(self._income.values())}"
    profit = Position ("Alex", "Max", "Anna", 50000, 100000)
    print (profit.get_full_name())
    print (prifit.get_total_income())
    print (profet.Position())
