# (2009). Introduction to algorithms. Cambridge, Mass: MIT Press.
#
# Section 15.2 Matrix-chain multiplication
#
# Let S(n) denote the minimal operations needed for n matrices.
#
# S(n) = min(S(0, i) + S(i+1, n) + "operations of the two multiplied")
#
# For rod cutting problem, only length is important, so we use S(n) to
# denote the best price of length n. Here length is not enough, thus
# we must explicitly specify the range of matrices. We have to use a
# 2-d table for caching the sub-answers.


def min_ops(matrices):
    matrices_count = len(matrices)
    ops = [[0 for row in range(matrices_count)]
           for row in range(matrices_count)]
    cut_pos = [[(0, 0) for row in range(matrices_count)]
               for row in range(matrices_count)]
    for i in range(1, matrices_count):
        for j in range(0, matrices_count - i):
            # The weird indexing is to access from the diagonal.
            #
            # 1 2 3 4
            # 0 1 2 3
            # 0 0 1 2
            # 0 0 0 1
            #
            # First 2, 2, 2, then 3, 3, finally 4.

            row = j
            col = j + i
            min_muls = float("inf")
            for cut in range(row, col):
                cur_ops = ops[row][cut] + ops[cut + 1][col] + \
                    matrices[row][0] * matrices[cut][1] * matrices[col][1]
                if min_muls > cur_ops:
                    min_muls = cur_ops
                    cut_pos[row][col] = cut
            ops[row][col] = min_muls
            print("({}, {}): {}".format(row, col, min_muls))

    # print(ops)
    parenthesized = str_parenthesized(matrices, cut_pos,
                                      (0, matrices_count - 1))
    print(parenthesized)
    return ops[0][matrices_count - 1]


def str_parenthesized(matrices, cut_pos, range):
    begin = range[0]
    end = range[1]
    if begin == end:
        return "{}".format(matrices[begin])

    pos = cut_pos[range[0]][range[1]]
    s1 = str_parenthesized(matrices, cut_pos, (range[0], pos))
    s2 = str_parenthesized(matrices, cut_pos, (pos + 1, range[1]))
    return "({} x {})".format(s1, s2)


def test_1():
    matrices = [(10, 100), (100, 5), (5, 50)]
    assert (min_ops(matrices) == 7500)


def test_2():
    matrices = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
    assert (min_ops(matrices) == 15125)
