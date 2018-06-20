#include <cstdint>
#include <cassert>
using namespace std;


class Solution
{
  public:
    int hammingWeight(uint32_t n)
    {
        uint32_t bits = n;
        int oneCount = 0;
        while(bits > 0){
            uint32_t bit = bits & 0x1;
            if(bit == 1){
                oneCount++;
            } 
            bits = bits >> 1;
        }
        
        return oneCount;
    }
};


int main(int argc, char const *argv[])
{
    Solution solution;
    assert(1 == solution.hammingWeight(1));
    assert(1 == solution.hammingWeight(2));
    assert(2 == solution.hammingWeight(3));
    assert(1 == solution.hammingWeight(4));
    assert(3 == solution.hammingWeight(11));
    return 0;
}
