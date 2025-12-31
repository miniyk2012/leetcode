import inspect


# 题目: h,m,n是3个字符串, 计算h m在n中同时出现的次数, h在m之前且无交叉

def count_h_m_before(n: str, h: str, m: str) -> int:
    """
    统计h、m在n中同时出现，且h在m前、无交叉的次数
    :param n: 主字符串
    :param h: 子串h
    :param m: 子串m
    :return: 符合条件的次数
    """
    if not h or not m or len(n) < len(h) + len(m):
        return 0  # 边界：h/m为空，或主串长度不足

    h_len = len(h)
    m_len = len(m)
    count = 0

    # 第一步：找到所有h在n中的结束位置（h_end = h_start + h_len）
    h_ends = []
    for i in range(len(n) - h_len + 1):
        if n[i:i + h_len] == h:
            h_ends.append(i + h_len)  # 记录h的结束索引（下一个字符的位置）

    # 第二步：对每个h的结束位置，统计之后出现的m的次数
    for h_end in h_ends:
        # m的起始位置需 ≥ h_end，且m的结束位置 ≤ len(n)
        for j in range(h_end, len(n) - m_len + 1):
            if n[j:j + m_len] == m:
                count += 1

    return count


def func(x, y=10):
    ...

# 测试示例
if __name__ == "__main__":
    # 测试用例1：n="abchmdefm", h="ch", m="m" → h结束在索引5，之后有2个m → 结果2
    print(count_h_m_before("abchmdefm", "ch", "m"))  # 输出：2
    # 测试用例2：n="hmhm", h="h", m="m" → (h0,m1)、(h0,m3)、(h2,m3) → 结果3
    print(count_h_m_before("hmhm", "h", "m"))  # 输出：3
    # 测试用例3：n="hmmh", h="h", m="m" → (h0,m1)、(h0,m2) → 结果2
    print(count_h_m_before("hmmh", "h", "m"))  # 输出：2

