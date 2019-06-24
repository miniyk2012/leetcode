/*
undo / redo

stack = [action1, action2]
redo = [action3]

state = reduce(stack)
 */
// 回到某个状态，就是把最后的动作出栈，然后reduce从起的动作，得到旧的状态 快捷键back, forward的实现就可以这么搞
// 不过每次都需要从头reduce是不是效率太低了？

// 列表可以当做stack，也可以当做queue来用
// 比如一个循环播放多幅画面的展示栏



// UI / View

// [A B C D]
// [B C D A]
// [C D A B]



// Model
// 环形链表比较方便，用普通链表的话
// ll = LinkedList(1,2,3,4)
// a = ll.pop()
// ll.push(a)
// 环形链表：保存2个状态：head和len即可


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
        },
        sortedAdd: function(v) {
            if (!this.head) {
                this.head = Node(v)
                return
            }
            this.head = this.head.sortedAdd(v)
        }
    }
}

function Node(v) {
    return {
        v: v,
        next: null,
        first: function(n) {
            if ( n <=0 )
                return []
            let ret = [this.v]
            if ( this.next ) {
                let r = this.next.first(n-1)
                ret.push(...r)  // ret.push(r[0], r[1], ...)
                return ret
            }
            return ret
        },
        sortedAdd: function(v) {
            if ( this.v >= v ) {
                let n = Node(v)
                n.next = this
                return n
            } else if ( !this.next || v < this.next.v ) {
                let n = Node(v)
                let tmp = this.next
                this.next = n
                n.next = tmp
                return this
            } else {
                return this.next.sortedAdd(v)
            }
        }
    }
}

let l = LinkedList()
l.add(1)
l.add(2)
l.add(3)


let a = l.popHead()
console.log('--', a)
l.add(a)
let r = l.first(3)
console.log(r)

a = l.popHead()
console.log('--', a)
l.add(a)
r = l.first(3)
console.log(r)

a = l.popHead()
console.log('--', a)
l.add(a)
r = l.first(3)
console.log(r)

a = l.popHead()
console.log('--', a)
l.add(a)
r = l.first(3)
console.log(r)

console.log('sortAdd')

let nl = LinkedList()
nl.sortedAdd(5)
nl.sortedAdd(10)
nl.sortedAdd(3)
nl.sortedAdd(2)

nr = nl.first(3)
console.log(nr)
// Controller