
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
        popHead: function() {
            if (!this.head) {
                console.log('链表为空')
                return
            }
            let oldHead = this.head
            this.head = this.head.next
            oldHead.next = null
            return oldHead.v
        },
        first: function(n) {
            // 返回起始的n个元素
            if (this.head)
                return this.head.first(n)
        }
    }
}

function Node(v) {
    return {
        v: v,
        next: null,
        first: function*(n) {  // js的生成器
            yield this.v
            if ( this.next && n > 1 ) {
                yield *this.next.first(n-1)
            }
        }
    }
}

let l = LinkedList()
l.add(1)
l.add(2)
l.add(3)

let a = l.first(3)
let n = a.next()
while ( !n.done ) {
    console.log(n.value)
    n = a.next()
}
console.log(n)