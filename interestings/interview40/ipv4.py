import re


class IPV4Parser:

    def is_valid_part(self, part: str):
        """判断每个区间是否是有效的"""
        if part in ('*', '0'):
            return True
        try:
            int_val = int(part)
            if part[0] != '0' and 0 < int_val <= 255:
                return True
        except ValueError:
            return False
        return False

    def is_valid_ipv4(self, ip: str):
        ip_parts = ip.split('.')
        if len(ip_parts) != 4:
            return False
        return all(self.is_valid_part(part) for part in ip_parts)

    def provide_all_seem_ipv4s(self, text):
        """给出所有xx.xx.xx.xx形式的子字符串"""
        i = 0
        while True:
            if i >= len(text):
                break
            dot_num = 0
            for j in range(i, len(text)):
                if text[j] == '.':
                    dot_num += 1
                if dot_num == 3:
                    yield text[i:j + 1]
                if dot_num == 4:
                    i += 1
                    break
            else:
                i += 1

    def parse_ipv4(self, text):
        ipv4_set = set()
        ipv4_list = []
        for seem in self.provide_all_seem_ipv4s(text):
            if self.is_valid_ipv4(seem):
                if seem not in ipv4_set:
                    ipv4_set.add(seem)
                    ipv4_list.append(seem)
        return ipv4_list


if __name__ == '__main__':
    parser = IPV4Parser()
    result = parser.parse_ipv4('129.8.7.634.23.*.23')
    print(result)
