// Problem ID: 2796
// Title: Allow One Function Call
// Runtime: 49 ms

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var hasBeenCalled = false;
    return function(...args){
        if (!hasBeenCalled){
            hasBeenCalled = true;
            return fn(...args);
        }
        else{
            return undefined;
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
