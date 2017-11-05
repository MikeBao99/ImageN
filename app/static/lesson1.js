
  var myCodeMirror = CodeMirror(document.querySelector("#linear1"), {
    value: "\ndef linear_search(search_list, target):\n    for x in range(len(search_list)):\n        if(search_list[x] == target) :\n            print(x)\n            return",
    mode:  "python",
    theme: "xq-light"
  });


