undo / redo

stack = [action1, action2]
redo = [action3]

state = reduce(stack)
// 回到某个状态，就是把最后的动作出栈，然后reduce从起的动作，得到旧的状态 快捷键back, forward的实现就可以这么搞
// 不过每次都需要从头reduce是不是效率太低了？

// 列表可以当做stack，也可以当做queue来用
// 比如一个循环播放多幅画面的展示栏



// UI / View

// [A B C D]
// [B C D A]
// [C D A B]



// Model




// Controller
