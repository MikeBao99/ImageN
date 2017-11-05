
  var myCodeMirror = CodeMirror(document.querySelector("#selectionsortcode"), {
    value: "\nlist = [17, 15, 14, 23, 28, 24, 19, 13, 26, 18]\n\nfor i in range(len(list)):\n    minindex = i\n    for j in range(i+1, len(list)):\n        if list[minindex] > list[j]:\n            minindex = j\n    list[i], list[minindex] = list[minindex], list[i]\n\nfor i in range(len(list)):\n    print(list[i])",
    mode:  "python",
    theme: "xq-light"
  });


