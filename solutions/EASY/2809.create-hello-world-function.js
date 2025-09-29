// Problem ID: 2809
// Title: Create Hello World Function
// Runtime: 54 ms

/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */