
  var myCodeMirror = CodeMirror(document.querySelector("#recurse"), {
    value: "def factorial(n) :\n    if n > 1 :\n        return n * factorial(n-1)\n    elif n == 0 :\n        return 1\n",
    mode:  "python",
    theme: "xq-light"
  });


