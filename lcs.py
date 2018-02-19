# (2009). Introduction to algorithms. Cambridge, Mass: MIT Press.
#
# Section 15.4 Longest common subsequence


def lcs(a, b):
    len1 = len(a)
    len2 = len(b)
    table = [[0 for col in range(len2 + 1)] for row in range(len1 + 1)]

    for row in range(1, len1 + 1):
        for col in range(1, len2 + 1):
            # print("row: {}, col: {}".format(row, col))
            if a[row - 1] == b[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
            else:
                table[row][col] = max(table[row - 1][col], table[row][col - 1])

    return get_lcs(a, b, table, (len1, len2))


def get_lcs(a, b, table, pos):
    row = pos[0]
    col = pos[1]

    if row == 0 or col == 0:
        return ''

    if table[row][col] == table[row - 1][col - 1] + 1:
        s = get_lcs(a, b, table, (row - 1, col - 1))
        return s + a[row - 1]
    else:
        if table[row - 1][col] >= table[row][col - 1]:
            return get_lcs(a, b, table, (row - 1, col))
        else:
            return get_lcs(a, b, table, (row, col - 1))


def test_1():
    x = 'ABCBDAB'
    y = 'BDCABA'
    assert (lcs(x, y) == 'BCAB')
