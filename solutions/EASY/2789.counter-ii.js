// Problem ID: 2789
// Title: Counter II
// Runtime: 51 ms

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var temp = init;
    return {
        increment : () => {
            temp += 1;
            return temp;
        },
        decrement : () => {
            temp-=1;
            return temp;
        },
        reset : () => {
            temp = init;
            return temp;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */