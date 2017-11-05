
  var myCodeMirror = CodeMirror(document.querySelector("#binary"), {
    value: "def binary_search(sorted_list, target) :\n    minimum = 0\n    maximum = len(sorted_list) - 1\n    while minimum <= maximum :\n        middle = (minimum+maximum)/2\n        compare = sorted_list[middle]\n        if  compare > target :\n            maximum = middle - 1\n        elif compare < target :\n            minimum = middle + 1\n        else :\n            return middle\n    return -1",
    mode:  "python",
    theme: "xq-light"
  });


