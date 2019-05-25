package main

import "fmt"

type Node struct {
	v int
	next *Node
}

func (n *Node) add(val int) {
	if n.next == nil {
		n.next = &Node{v: val}
		return
	}
	cur := n.next
	for cur.next != nil {
		cur = cur.next
	}	
	cur.next = &Node{v: val}
}

func (n *Node) print() {
	for cur := n; cur != nil; cur = cur.next {
		fmt.Println(cur.v)
	}
}


func main() {
	n := Node{v: 10}
	n.add(2)
	n.add(3)
	n.add(4)
	n.print()
}