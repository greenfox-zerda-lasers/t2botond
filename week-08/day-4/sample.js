var test = require('tape');

var add = function (a, b) {
  return a + b;
}

test('add 2 numbers', function (t) {
    var actual = add(1, 2);
    var expected = 3;

    t.equal(actual, expected);
    t.end();
});
