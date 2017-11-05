
  var myCodeMirror = CodeMirror(document.querySelector("#bubblesortcode"), {
    value: "\nlist = [17, 15, 14, 23, 28, 24, 19, 13, 26, 18]\n\nfor i in range(len(list)):\n    for j in range(0, len(list)-1):\n        if list[j] > list[j+1]:\n            list[j], list[j+1] = list[j+1], list[j]\n\nfor i in range(len(list)):\n    print(list[i])",
    mode:  "python",
    theme: "xq-light"
  });


