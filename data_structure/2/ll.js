function LinkedList() {
    return {
        head: null,
        add: function(v) {
            if (!this.head) {
                this.head = Node(v)
                return
            }
            let cur = this.head
            while (cur.next) {
                cur = cur.next
            }
            cur.next = Node(v)
        },
        print: function() {
            let cur = this.head
            while (cur) {
                console.log(cur.v)
                cur = cur.next
            }
        },
        pop: function() {
            if (!this.head) {
                console.log('链表为空')
                return
            }
            let oldHead = this.head
            this.head = this.head.next
            oldHead.next = null
            return oldHead.v
        }
    }
}

function Node(v) {
    return {
        v: v,
        next: null
    }
}


l = LinkedList()
l.add(10)
l.add(-2)
l.print()
console.log('pop:')
v = l.pop()
console.log(v)
console.log('after pop:')
l.print()
