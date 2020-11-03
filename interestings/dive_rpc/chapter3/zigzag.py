from interestings.dive_rpc.chapter3.varint import VarInt


class ZigZag:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def encode(int_value: int):
        if int_value >= 0:
            return VarInt.encode(int_value * 2)
        else:
            return VarInt.encode(abs(int_value) * 2 - 1)

    @staticmethod
    def decode(bytes_value: bytes):
        int_value = VarInt.decode(bytes_value)
        if ZigZag.is_even(int_value):
            return int_value // 2
        else:
            return -(int_value + 1) // 2
