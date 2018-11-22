import array


class RecentCounter:
    def __init__(self):
        self.serials = array.array("L")

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        serials = self.serials
        count = len(serials)
        min_t = t - 3000
        start_index = count
        i = 0
        while i < count:
            if serials[i] < min_t:
                i += 1
                continue
            else:
                start_index = i
                break

        serials = serials[start_index:]
        serials.append(t)
        self.serials = serials
        return len(serials)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


def test_RecentCounter():
    # for i in range(100):

    obj = RecentCounter()
    assert obj.ping(642) == 1
    assert obj.ping(1849) == 2
    assert obj.ping(4921) == 1
    assert obj.ping(5936) == 2
    assert obj.ping(5937) == 3

    obj2 = RecentCounter()
    assert obj2.ping(1) == 1
    assert obj2.ping(100) == 2
    assert obj2.ping(3001) == 3
    assert obj2.ping(3002) == 3