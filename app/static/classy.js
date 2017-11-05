
  var myCodeMirror = CodeMirror(document.querySelector("#class"), {
    value: "\nclass Pycat :\n    def __init__(self, name, age) :\n        self_name = name\n        self_age = age\n    def meow(self) :\n        print 'Meow'\n",
    mode:  "python",
    theme: "xq-light"
  });


