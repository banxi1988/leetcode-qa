
#include<stdlib.h>
#include<assert.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *result = malloc(sizeof(int) * 2);
    int first = 0;
    int second = 1;
    for(first = 0;first < numsSize;first++){
        // 后面如果再有0的话或者负数的话，这个优化不成立.
        // if(nums[first] > target){
        //     continue;
        // }
        for(second = first + 1; second < numsSize;second++){
                if((nums[first] + nums[second]) == target){
                    result[0] = first;
                    result[1] = second;
                    return result;
                }
        }
    }
    return NULL;
}

int main(){
    int nums[] = {2,7,11,15};
    int target = 9;
    int numsSize = 4;
    int* indices = twoSum(nums,numsSize, target);
    assert(indices[0] == 0);
    assert(indices[1] == 1);

    indices = twoSum(nums,numsSize,26);
    assert(indices[0] == 2);
    assert(indices[1] == 3);

    indices = twoSum(nums,numsSize,17);
    assert(indices[0] == 0);
    assert(indices[1] == 3);

    indices = twoSum(nums,numsSize,13);
    assert(indices[0] == 0);
    assert(indices[1] == 2);

    indices = twoSum(nums,numsSize,18);
    assert(indices[0] == 1);
    assert(indices[1] == 2);

    int nums2[] = {0,4,2,0};
    indices = twoSum(nums2,4,0);
    assert(indices[0] == 0);
    assert(indices[1] == 3);

    int nums3[] = {-1,-2,-3,-4,-5};
    indices = twoSum(nums3,5,-8);
    assert(indices[0] == 2);
    assert(indices[1] == 4);
    return 0;
}