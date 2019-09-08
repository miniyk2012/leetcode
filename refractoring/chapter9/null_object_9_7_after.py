import abc


class Nullable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_null(self):
        pass


class PaymentHistory:
    def __init__(self, delinquent: int = 0):
        self._delinquent = delinquent

    def get_weeks_delinquent_in_last_year(self):
        return self._delinquent


class Customer(Nullable):
    def is_null(self):
        return False

    def __init__(self, name: str, plan: str, payment_history: PaymentHistory):
        self.name = name
        self.plan = plan
        self.payment_history = payment_history

    @property
    def name(self):
        return self._name or "Unknown"

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def plan(self):
        return self._plan or "Basic Plan"

    @plan.setter
    def plan(self, value):
        self._plan = value

    @property
    def payment_history(self) -> PaymentHistory:
        return self._payment_history or PaymentHistory()

    @payment_history.setter
    def payment_history(self, value):
        self._payment_history = value


class NullCustomer(Customer, Nullable):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'Unknown'

    @property
    def plan(self):
        return "Basic Plan"

    @property
    def payment_history(self) -> PaymentHistory:
        return PaymentHistory()

    def is_null(self):
        return True


class Site:
    def __init__(self, customer: Customer = None):
        self._customer = customer

    @property
    def customer(self) -> Customer:
        return self._customer or NullCustomer()

    @customer.setter
    def customer(self, value: Customer):
        self._customer = value
