# (2009). Introduction to algorithms. Cambridge, Mass: MIT Press.
#
# Section 15.1 Rod cutting, page 360
#
# Let S(n) denote the best price of length n.
#
# S(n) = min(price_as_a_whole[n], S[i] + S[n-i]) for i in [1..n-1]

price_table = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod(length):
    best_price = [0 for i in range(length + 1)]
    cut_pos = [0 for i in range(length + 1)]
    for i in range(length + 1):
        max_price = 0
        if i < len(price_table):
            max_price = price_table[i]

        cut_pos[i] = 0
        for j in range(1, int(i / 2) + 1):
            if best_price[j] + best_price[i - j] > max_price:
                max_price = best_price[j] + best_price[i - j]
                cut_pos[i] = j
        best_price[i] = max_price

    cuts = construct(cut_pos, length)
    return (best_price[length], cuts)


def construct(cut_pos, length):
    pos = cut_pos[length]
    if pos == 0:
        return [length]

    sub1 = construct(cut_pos, pos)
    sub2 = construct(cut_pos, length - pos)
    return sub1 + sub2


def test_1():
    (price, cuts) = cut_rod(4)
    assert (price == 10)
    assert (cuts == [2, 2])


def test_2():
    price, cuts = cut_rod(5)
    assert (price == 13)
    assert (cuts == [2, 3])


def test_3():
    price, cuts = cut_rod(7)
    assert (price == 18)
    assert (cuts == [1, 6] or cuts == [2, 2, 3])


def test_4():
    price, cuts = cut_rod(40)
    assert (price == 120)
    assert (cuts == [10, 10, 10, 10])
