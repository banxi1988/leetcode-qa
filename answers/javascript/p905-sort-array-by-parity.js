/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function (A) {
    const evens = A.filter(it => it % 2 === 0)
    const odds = A.filter(it => it % 2 !== 0)
    return evens.concat(odds)
};