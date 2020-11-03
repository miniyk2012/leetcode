from functools import reduce


class VarInt:
    offset = 7
    varint_data_byte_bits = 0x7f
    varint_exists_next_byte_bit = 0x80

    @classmethod
    def encode(cls, int_value: int):
        every_bytes = bytearray()

        while True:
            if int_value == 0 and len(every_bytes) > 0:
                break
            first_bytes = int_value & cls.varint_data_byte_bits

            every_bytes.append(first_bytes)
            int_value >>= cls.offset  # 每次右移7位

        for idx in range(len(every_bytes) - 1):  # 除了最后一个字节外,其他字节首位置为1
            every_bytes[idx] |= cls.varint_exists_next_byte_bit
        return bytes(every_bytes)

    @classmethod
    def decode(cls, bytes_value: bytes):
        every_bytes = bytearray(bytes_value)

        for idx in range(len(every_bytes) - 1):
            every_bytes[idx] &= cls.varint_data_byte_bits
        every_bytes.reverse()

        return reduce(lambda x, y: x << cls.offset | y, every_bytes)


if __name__ == '__main__':
    encoded = VarInt.encode(128)
    print(encoded.hex())
    print(VarInt.decode(encoded))
