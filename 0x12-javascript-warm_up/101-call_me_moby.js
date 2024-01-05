#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  for (let i = x; i > 0; i--) {
    theFunction();
  }
};
