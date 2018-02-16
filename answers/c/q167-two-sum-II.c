
#include<stdlib.h>
#include<assert.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int *result = calloc(*returnSize,sizeof(int));
    int first = 0;
    int second = 1;
    int remind = 0;
    for(first = 0;first < numbersSize;first++){
        if(numbers[first] > target){
            continue;
        }
        remind = target - numbers[first];
        for(second = first + 1; second < numbersSize;second++){
            if(numbers[second] > remind){
                break;
            }
                if((numbers[first] + numbers[second]) == target){
                    result[0] = first + 1;
                    result[1] = second + 1;
                    return result;
                }
        }
    }
    return result;
}

int main(){
    int nums[] = {2,7,11,15};
    int target = 9;
    int numsSize = 4;
    int returnSizeValue[] = {2};
    int* returnSize = returnSizeValue;
    int* indices = twoSum(nums,numsSize, 9,returnSize);
    assert(indices[0] == 1);
    assert(indices[1] == 2);


    int nums2[] = {0,0,2,4};
    indices = twoSum(nums2,4,0,returnSize);
    assert(indices[0] == 1);
    assert(indices[1] == 2);

    int nums3[] = {1,2,3,4,5};
    indices = twoSum(nums3,5,8,returnSize);
    assert(indices[0] == 3);
    assert(indices[1] == 5);

    int nums4[] = {2,3,4};
    indices = twoSum(nums4,3,6,returnSize);
    assert(indices[0] == 1);
    assert(indices[1] == 3);
    return 0;
}