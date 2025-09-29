// Problem ID: 2732
// Title: Counter
// Runtime: 46 ms

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var count = n-1;
    return function() {
        count+=1;
        return count;
    };
    
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */