import abc


class Statement(abc.ABCMeta):
    @classmethod
    def value(cls, customer):
        result = cls.header_string(customer)

        for retal in customer.rentals:
            result += cls.each_rental_string(retal)

        result += cls.footer_string(customer)
        return result

    @staticmethod
    @abc.abstractmethod
    def header_string(customer):
        """表头"""
        pass

    @staticmethod
    @abc.abstractmethod
    def each_rental_string(retal):
        """展示一条影片租赁的详情"""
        pass

    @staticmethod
    @abc.abstractmethod
    def footer_string(customer):
        """汇总信息"""
        pass


class TextStatment(Statement):
    @staticmethod
    def header_string(customer):
        return "Rental Record for " + customer.get_name() + "\n"

    @staticmethod
    def each_rental_string(retal):
        return "\t" + retal.get_movie().get_title() + "\t" \
               + str(retal.get_charge()) + "\n"

    @staticmethod
    def footer_string(customer):
        return "Amount owned is " + str(customer.get_total_charge()) + "\n" \
               + "You earned " + str(customer.get_total_frequent_point()) \
               + " frequent renter points"
