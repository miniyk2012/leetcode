package main

import "fmt"

type Node struct {
	v int
	next *Node
}

type LinkedList struct {
	head *Node
}



func (l *LinkedList) add(val int) {
	if l.head == nil {
		l.head = &Node{v: val}
		return
	}
	cur := l.head
	for cur.next != nil {
		cur = cur.next
	}	
	cur.next = &Node{v: val}
}

func (l *LinkedList) print() {
	for cur := l.head; cur != nil; cur = cur.next {
		fmt.Println(cur.v)
	}
}

func (l *LinkedList) popHead() *Node {
	n := l.head
	l.head = n.next
	n.next = nil
	return n
}

func main() {
	l := LinkedList{head: nil}
	l.add(-2)
	l.add(5)
	l.add(3)
	l.add(4)
	l.print()
	n := l.popHead()
	fmt.Printf("head val is %d\n", n.v)
	l.print()
}