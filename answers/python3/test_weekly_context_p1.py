class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        key_to_log = {}
        num_logs = []
        keys = []
        for log in logs:
            comps = log.split(" ")
            if comps[1][0].isdigit():
                num_logs.append(log)
            else:
                key = " ".join(comps[1:])
                keys.append(key)
                key_to_log[key] = log
        keys.sort(reverse=False)
        result_logs = []
        for key in keys:
            log = key_to_log[key]
            result_logs.append(log)

        return result_logs + num_logs


def test_wc110_p1():
    input1 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    expected_output1 = [
        "g1 act car",
        "a8 act zoo",
        "ab1 off key dog",
        "a1 9 2 3 1",
        "zo4 4 7",
    ]
    solution = Solution()
    assert solution.reorderLogFiles(input1) == expected_output1

    input2 = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
    output2 = ["5 m w", "j mo", "t q h", "g 07", "o 2 0"]
    assert solution.reorderLogFiles(input2) == output2

    input3 = [
        "ond 5092781 316 6704",
        "8qt 089 1 505824730",
        "ty szwmdr fqf nlums",
        "06hy thfo ofhdibrnc",
        "f 341750204886995331",
        "rab lxyhr xhlpkk t q",
        "54a 4 240 48299311 0",
        "nqp2o jrlokgypqh op",
        "jxc lafwu p ctjjj vv",
        "6c 944639313298 221",
        "hd6 dhdhajyqylb m c",
        "qp 5014057259194839",
        "3ljd2 cbvoeej da lro",
        "6lxa l xrvmcmsfdzlq",
        "zotrq 19964 46917945",
        "7m cecsiar vxp yksaq",
        "uktnk mgaa hbvc vt t",
        "p3 lseldodyxhiazo z",
        "xp sgiea f r mhnsqeu",
        "syufn 7 54169586 8 9",
    ]
    output3 = [
        "3ljd2 cbvoeej da lro",
        "7m cecsiar vxp yksaq",
        "hd6 dhdhajyqylb m c",
        "nqp2o jrlokgypqh op",
        "6lxa l xrvmcmsfdzlq",
        "jxc lafwu p ctjjj vv",
        "p3 lseldodyxhiazo z",
        "rab lxyhr xhlpkk t q",
        "uktnk mgaa hbvc vt t",
        "xp sgiea f r mhnsqeu",
        "ty szwmdr fqf nlums",
        "06hy thfo ofhdibrnc",
        "ond 5092781 316 6704",
        "8qt 089 1 505824730",
        "f 341750204886995331",
        "54a 4 240 48299311 0",
        "6c 944639313298 221",
        "qp 5014057259194839",
        "zotrq 19964 46917945",
        "syufn 7 54169586 8 9",
    ]
    assert solution.reorderLogFiles(input3) == output3
