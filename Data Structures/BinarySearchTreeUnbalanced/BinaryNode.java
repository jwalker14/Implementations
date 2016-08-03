package BSTU;

class BinaryNode{
	private Integer el;
	private BinaryNode left;
	private BinaryNode right;

	public BinaryNode(){
		node(null,null,null);
	}

	public BinaryNode(Integer x){
		node(x,null,null);
	}

	public BinaryNode(Integer x, BinaryNode l, BinaryNode r){
		node(x,l,l);
	}

	public void node(Integer x, BinaryNode l, BinaryNode r){
		this.el = x;
		this.left = l;
		this.right = r;
	}

	public void set_left(BinaryNode l){
		this.left = l;
	}

	public void set_right(BinaryNode r){
		this.right = r;
	}

	public void set_element(Integer i){
		this.el = i;
	}

	public BinaryNode get_left(){
		return this.left;
	}

	public BinaryNode get_right(){
		return this.right;
	}

	public Integer get_element(){
		return this.el;
	}
}