
  var myCodeMirror = CodeMirror(document.querySelector("#bstnode"), {
    value: "\nclass Node(object):\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right",
    mode:  "python",
    theme: "xq-light"
  });

  var myCodeMirror = CodeMirror(document.querySelector("#bstconst"), {
    value: "\nroot = Node(15)\nroot.left = Node(11)\nroot.left.left = Node(6)\nroot.left.right = Node(14)\nroot.right = Node(20)\nroot.right.left = Node(17)\nroot.right.right = Node(28)",
    mode:  "python",
    theme: "xq-light"
  });

  var myCodeMirror = CodeMirror(document.querySelector("#bstsearch"), {
    value: "\ndef bstsearch(cur, val):\n    if(cur == None):\n        return\n    if(cur.value == val):\n        print(\"Found!\")\n        return\n    if(val < cur.value):\n        bstsearch(cur.left, val)\n    elif(val > cur.value):\n        bstsearch(cur.right, val)",
    mode:  "python",
    theme: "xq-light"
  });

  var myCodeMirror = CodeMirror(document.querySelector("#bstfull"), {
    value: "class Node(object):\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\n\nroot = Node(15)\nroot.left = Node(11)\nroot.left.left = Node(6)\nroot.left.right = Node(14)\nroot.right = Node(20)\nroot.right.left = Node(17)\nroot.right.right = Node(28)\n\ndef bstsearch(cur, val):\n    if(cur == None):\n        return\n    if(cur.value == val):\n        print(\"Found!\")\n        return\n    if(val < cur.value):\n        bstsearch(cur.left, val)\n    elif(val > cur.value):\n        bstsearch(cur.right, val)\n\nbstsearch(root, 14) # Found!\nbstsearch(root, 16) # Not found",

    mode:  "python",
    theme: "xq-light"
  });

