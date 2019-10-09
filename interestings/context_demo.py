from contextlib import contextmanager


class Connction:

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def close(self):
        print("close conn")

    def get_cursor(self):
        return Cursor()


class Cursor:

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def close(self):
        print("close cursor")


@contextmanager
def outer():
    conn = Connction()
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def inner():
    with outer() as conn:
        cursor = conn.get_cursor()
        try:
            yield cursor
        finally:
            cursor.close()




if __name__ == '__main__':
    with inner() as cursor:
        print("trans")

    print("*" * 100)

    with Connction() as conn, conn.get_cursor() as cursor:
        print("trans")

    print("*" * 100)

    generator = inner().func()
    try:
        cursor = next(generator)
        print(cursor)
        next(generator)
    except StopIteration:
        pass

    print("*" * 100)
    with inner() as cursor:
        print("befor trnas")
        raise RuntimeError("ha")
        print("trans")
