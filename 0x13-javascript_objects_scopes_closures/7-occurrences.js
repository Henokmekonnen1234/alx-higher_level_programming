#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, x) => {
    if (x === searchElement) {
      count++;
    }
    return count;
  }, 0);
};
