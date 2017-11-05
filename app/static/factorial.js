
  var myCodeMirror = CodeMirror(document.querySelector("#factorialcode"), {
    value: " \ndef factorial_1(int n):\n  product = 1\n  for i in range(1, n+1):\n    product *= i\n  return product\n\n\ndef factorial_2(int n):\n  if n==0:\n    return 1\n  return factorial_2(n-1)",
    mode:  "python",
    theme: "xq-light"
  });


