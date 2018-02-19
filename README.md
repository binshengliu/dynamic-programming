# Dynamic Programming [![Build Status](https://travis-ci.org/lbsx/dynamic-programming.svg?branch=master)](https://travis-ci.org/lbsx/dynamic-programming)

Chapter 15 of Introduction to Algorithms 3rd Edition is about *Dynamic
Programming*. Rod cutting and matrix multiplication are two problems
used to introduce this technique. Before reading the answers, I tried
to solve them independently. This is the repository for my solutions
in Python.


<a id="orga6a0e93"></a>

## Chapter 15 Dynamic Programming

-   Dynamic programming solves problems that can be divided into
    sub-problems, which have **overlapping** sub-sub-problems.
-   It is usually applied to optimization problems.
-   Four steps of developing a dynamic programming algorithm.
    1.  Find the structure of the optimal solution.
    2.  **Recursively** define how the solution is made up of
        optimal solutions to sub-problems.
    3.  Compute the final value, usually in a bottom-up style.
    4.  Construct the solution.


<a id="orgdaebe9e"></a>

### Rod cutting

-   Given a rod of length n inches and a table of prices p<sub>i</sub> for i =
    1, 2, &#x2026;, n, determine the maximum revenue r<sub>n</sub> obtainable by
    cutting up the rod and selling the pieces.
-   Optimal structure
    1.  Once we make the first cut, we have two rod cutting
        subproblems. We must choose where to cut it first.
    2.  Suppose that position k is the best initial cut position.
    3.  Now we have two subproblems of cutting two rods of length k
        and n-k.
    4.  The solutions to k and n-k must also be optimal. Otherwise, we
        can find a better cutting for them and get a better final
        solution.
-   Recursive definition
    -   r<sub>n</sub> = max(price<sub>as_a_whole</sub>, r<sub>i</sub> + r<sub>n-i</sub>) for i = 1, 2, &#x2026;, n-1


<a id="org197b9fe"></a>

### Elements of dynamic programming


<a id="orgdadb17f"></a>

#### Optimal substructure

-   An optimal solution to a problem is constructed from optimal
    solutions to subproblems in a **recursive** manner.
-   A common pattern for discovering an optimal substructure.
    1.  Show that the solution consists of making a choice, which
        leaves one or more subproblems to be solved.
        -   In rod cutting problem, we choose where to cut the rod,
            leaving the subproblems of what are the optimal cuts of the
            two smaller pieces of rod.
    2.  Suppose that a choice is given to get the optimal solution.
        -   In rod cutting problem, we assume that we have a cut at
            position k that leads to the optimal cutting.
    3.  Determine which subproblems need to be solved
    4.  Show that solutions to the subproblems are also optimal.
        -   Suppose that the solutions to subproblems are not optimal
            and derive a contradiction.
        -   For example, in rod cutting problem, suppose we achieve the
            best cut for a rod (length i) at k (Step 2), so solutions
            to (0, k) and (k+1, i) must also be optimal. If they are
            not optimal, we have a better cut for (0, k) or (k+1, i)
            and get a better final solution, which contradicts our
            assumption that k is the best cut.


<a id="orgb717028"></a>

#### Overlapping subproblems

-   A recursive solution revisits the same subproblems repeatedly.
-   In dynamic programming technique, solutions to subproblems are
    computed once and stored. When a solved subproblem is revisited,
    the solution is simply looked up, instead of being recomputed.

