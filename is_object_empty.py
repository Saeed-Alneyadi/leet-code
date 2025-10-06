/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // Checks whether the object is null or undefined
    if (obj === null || typeof obj === 'undefined') {
        return false // Or handle this case as an error if needed
    }

    // Checks whether the object is array and length of it is zero so it return @true
    if (Array.isArray(obj) && obj.length === 0) {
        return true
    }

    // Checks whether the object is a plain object and has no enumerable properties
    return Object.keys(obj).length === 0 && obj.constructor === Object;
};
