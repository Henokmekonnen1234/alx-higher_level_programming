#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((_, index, array) => array[array.length - 1 - index]);
};
