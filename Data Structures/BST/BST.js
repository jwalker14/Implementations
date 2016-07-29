//if not working run: npm install --save-dev babel-preset-es2015 babel-preset-stage-0 -g

class Node{
  constructor(x){
    this.value = x;
    this.left = null;
    this.right = null;
    this.count = 1;
    console.log('Node Created')
  }
}


class BST{
  constructor(n){
    this.root = n;
  }

  insert_rec(n,x){                    //recursive call for insert
    if(n.value == x){                 //if the current node is equal to value
      n.count++;                      //this is what amazon was looking for
      return;                         //return don't do anything
    }
    if(x < n.value){
      if(n.left == null){
        n.left = new Node(x);
      }
      else{
        this.insert_rec(n.left, x);
      }
    }
    else{
      if(n.right == null){
        n.right = new Node(x);
      }
      else{
        this.insert_rec(n.right, x)
      }
    }

  }

  insert(x){
    this.insert_rec(this.root, x)     //non recursive call for rec (public)
  }

  get_root(){
    return this.root
  }
}


//for testing
var tree = new BST(new Node(Math.floor(Math.random() * 10000)));  //create a tree
for(var i = 0; i < 1000000; i++){                                 //insert some random variables
  tree.insert(Math.floor(Math.random() * 1000))
}

root = tree.get_root()                                            //get the root
console.log(root.left)                                      //console the left val