from Customer import Customer
from movie import Movie
from rental import Rental


def test():
    c_movie = Movie("CHILDRENS", Movie.CHILDRENS)
    r_movie = Movie("REGULAR", Movie.REGULAR)
    n_movie = Movie("NEW_REALEASE", Movie.NEW_REALEASE)

    c_rental = Rental(c_movie, 20)
    r_rental = Rental(r_movie, 20)
    n_rental = Rental(n_movie, 20)

    customer = Customer("CUSTOMER")
    customer.add_rental(c_rental)
    customer.add_rental(r_rental)
    customer.add_rental(n_rental)

    result = customer.text_statement()
    assert result == """Rental Record for CUSTOMER
	CHILDRENS	27.0
	REGULAR	29.0
	NEW_REALEASE	60
Amount owned is 116.0
You earned 4 frequent renter points"""


if __name__ == "__main__":
    test()
