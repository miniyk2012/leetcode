class PaymentHistory:
    def __init__(self, delinquent: int = 0):
        self._delinquent = delinquent

    def get_weeks_delinquent_in_last_year(self):
        return self._delinquent


class Customer:
    def __init__(self, name: str, plan: str, payment_history: PaymentHistory):
        self.name = name
        self.plan = plan
        self.payment_history = payment_history

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def plan(self):
        return self._plan

    @plan.setter
    def plan(self, value):
        self._plan = value

    @property
    def payment_history(self) -> PaymentHistory:
        return self._payment_history

    @payment_history.setter
    def payment_history(self, value):
        self._payment_history = value


class Site:
    def __init__(self, customer: Customer = None):
        self._customer = customer

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, value: Customer):
        self._customer = value
