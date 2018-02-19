# (2009). Introduction to algorithms. Cambridge, Mass: MIT Press.
#
# Section 15.5 Optimal binary search tree
#
# Here the key observation is that, for a tree containing [k_i, ...,
# k_j] to become a subtree, the depth of each node increases by 1. The
# original cost is (p_i * depth_i + ... + p_j * depth_j). Becoming a
# subtree, the total cost of the new subtree is (p_i * (depth_i + 1) +
# ... + p_j * (depth_j + 1)). The increment is (p_i + ... + p_j).
#
# For a tree with root node k_r, the total cost is the sum of the
# costs of each tree and their increments of becoming a subtree, plus
# the cost of the root itself.
#
# cost(k_r) = cost[i..r-1] + cost[r+1..j] + p_r + inc[i..r-1] + inc[r+1..j]
#             ^^^^           ^^^^           ^^^   ^^^           ^^^
#             left tree      right tree     self  left inc      right inc
#
# p_r + inc[i..r-1] + inc[r+1..j] can be reduced to sum_of_prob[i..j],
# which consists of both the increment of word probabilities(i to j)
# and missing probabilities(i-1 to j).
#
# There are edge cases when r == i: cost[i..i-1], and r == j:
# cost[j+1..j]. There is a smart handling in the textbook.
#
# Word    0    1    2    3    4    5
# prob      0.15 0.10 0.05 0.10 0.20
# miss 0.05 0.10 0.05 0.05 0.05 0.10


def construct_tree(word_prob, miss_prob):
    length = len(word_prob) - 1
    costs = [[float('inf') for i in range(length + 1)]
             for j in range(length + 1)]
    roots = [[None for i in range(length + 1)] for j in range(length + 1)]

    # Initialize costs with only one word.
    for i in range(1, length + 1):
        costs[i][i] = word_prob[i] + \
            2 * (miss_prob[i - 1] + miss_prob[i])
        roots[i][i] = i

    for i in range(1, length + 1):
        for j in range(1, length + 1 - i):
            row = j
            col = i + j

            # Whichever word is chosen as the root, the increment is
            # the same.
            increment = miss_prob[row - 1]
            for k in range(row, col + 1):
                increment += word_prob[k] + miss_prob[k]

            for root in range(row, col + 1):
                # The edge cases can be avoided by initializing the
                # costs table in a smart way. See the textbook for
                # details. Though, explicitly handling the edge cases
                # make the code more clear for me.
                if root == row:
                    cost = increment + costs[root + 1][col] + miss_prob[row
                                                                        - 1]
                elif root == col:
                    cost = increment + costs[row][root - 1] + miss_prob[col]
                else:
                    cost = increment + \
                        costs[row][root - 1] + \
                        costs[root + 1][col]

                if cost < costs[row][col]:
                    costs[row][col] = cost
                    roots[row][col] = root

    # for r in costs:
    #     print(r)

    # for r in roots:
    #     print(r)

    print("Minimal cost: {}".format(costs[1][length]))
    return costs[1][length]


def test_1():
    # Index 0 of word_prob is not used
    word_prob = [0.00, 0.15, 0.10, 0.05, 0.10, 0.20]
    miss_prob = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    min_cost = construct_tree(word_prob, miss_prob)
    assert (min_cost == 2.75)
