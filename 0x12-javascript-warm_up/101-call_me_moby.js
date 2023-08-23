#!/usr/bin/node

exports.repeat_func = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
