
# 松鼠生宝宝, 成长到第三个月才生, 每个月生一次(雌雄一对), 松鼠10个寿命.  一开始有1对0个月松鼠,
# 请问第n个月有几对松鼠


def calculate_squirrel_pairs(n):
    """
    计算第n个月的松鼠对数
    :param n: 目标月份（正整数）
    :return: 第n个月的松鼠对数
    """
    if n < 0:
        return 0  # 输入校验：月份不能为负
    # 初始化：age_groups[i] = i月龄的松鼠对数，初始1对0月龄
    age_groups = [1] + [0] * 9  # 索引0-9对应0-9月龄，初始仅0月龄有1对

    for month in range(1, n):
        # 1. 计算当月繁殖的新松鼠对数（3-9月龄的松鼠总数）
        breeders = sum(age_groups[2:10])  # 3-9月龄可繁殖，切片左闭右开
        new_pairs = breeders

        # 2. 所有松鼠月龄+1：移除9月龄（下月满10月龄死亡），其余右移一位
        # 新列表：0月龄先占位，1-9月龄 = 原0-8月龄
        new_age_groups = [0] + age_groups[:9]
        # 3. 填充当月新生的0月龄松鼠
        new_age_groups[0] = new_pairs
        # 4. 更新月龄分组
        age_groups = new_age_groups
    print(list(reversed(age_groups)))

    # 统计第n个月的总对数
    total_pairs = sum(age_groups)
    return total_pairs


def give_birth_num(n):
    counts_of_month = [1] + [0] * (n-1)
    for month in range(1, n):
        start, end = max(0, month-10), month-3
        breeders = 0
        if end >=0:
            breeders = sum(counts_of_month[start:end+1])
        counts_of_month[month] = breeders
    return sum(counts_of_month[-10:])

# 测试示例
if __name__ == "__main__":
    for target_month in range(1, 15):
        result = calculate_squirrel_pairs(target_month)
        result2= give_birth_num(target_month)
        print(f"第{target_month}个月的松鼠总对数：{result:}, {result2:}")