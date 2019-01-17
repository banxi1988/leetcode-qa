# coding: utf-8

# https://leetcode-cn.com/problems/knight-dialer/


class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        step_to_next = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2],
            0: [4, 6],
        }
        mod = pow(10, 9) + 7

        def dial(remain_steps: int):
            prior_case = [1] * 10
            current_case = [0] * 10
            current_num_hops = 1
            while current_num_hops <= remain_steps:
                current_case = [0] * 10
                current_num_hops += 1
                for i in range(0, 10):
                    if i == 5:
                        continue
                    next_moves = step_to_next[i]
                    for move in next_moves:
                        count = current_case[i] + prior_case[move]
                        current_case[i] = count % mod
                prior_case = current_case
            return current_case

        nstep_cases = dial(N - 1)
        result = 0
        for count in nstep_cases:
            result += count
            result %= mod

        return result


def test_kniht_dialer():
    s = Solution()
    assert s.knightDialer(1) == 10
    assert s.knightDialer(2) == 20
    assert s.knightDialer(3) == 46
    assert s.knightDialer(4) == 104
    # assert s.knightDialer(100)
    # assert s.knightDialer(5000)


if __name__ == "__main__":
    test_knight_dialer()

