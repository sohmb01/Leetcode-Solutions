// Problem ID: 2761
// Title: Array Reduce Transformation
// Runtime: 55 ms

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    
    if (nums.length === 0){
        return init;
    }
    let val = function(prevVal, element){
        return fn(preVal,element);
    }
    let preVal = init;
    nums.forEach((element,index) => {
        ans = val(preVal,element);
        preVal = ans;
    });
    return ans;
};