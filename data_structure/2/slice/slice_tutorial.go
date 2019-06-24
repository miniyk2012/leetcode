package main

import "fmt"
type V struct {
	x int
}

func main() {
	l := []int{1,2,3}
	fmt.Println(l)
	a := [4]int{}
	z := a[:]
	b := a
	c := V{}
	d := c
	c.x = 10
	b[0] = 4
	a[0] = 10
	z[3] = -2
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(len([]int{}))
	fmt.Println(len([...]int{}))
	z = append(z, 5)
	fmt.Println(len(z))
	fmt.Println(len(z))
	fmt.Println(len(a))
	fmt.Println(cap(a))
	z[1] = 20
	fmt.Println(z)
	fmt.Println(a)
	m := z
	fmt.Printf("m slice: %v slice addr %p \n", m, &m)
	fmt.Printf("z slice: %v slice addr %p \n", z, &z)
	a1 := []int{1,2,3}
	a1 = append(a1, 2)
	fmt.Println(a1)
	fmt.Println(cap(a1))
	b1 := a1
	fmt.Printf("b slice: %v slice addr %p \n", b, &b)
	fmt.Printf("a slice: %v slice addr %p \n", a, &a)
	fmt.Println(cap(b1))
	a1 = append(a1, 12)
	fmt.Println(cap(a1))
	fmt.Println(cap(b1))
	b1 = b1[:cap(b1)]
	b1[4] = 10
	fmt.Println(a1)
	fmt.Println(b1)

	slice := []int{0, 1, 2, 3}
    fmt.Printf("slice: %v slice addr %p \n", slice, &slice)

    ret := changeSlice(slice)
	fmt.Printf("slice: %v ret: %v slice addr %p  ret addr %p\n", slice, ret, &slice, &ret)
	
	allocate()
}
func changeSlice(s []int) []int {
	fmt.Printf("s addr %p\n", &s)
    s[1] = 111
    return s
}

func allocate() {

    arr := [3]int{0, 1, 2}

    slice := arr[1:2]

    fmt.Printf("arr %v len %d, slice %v  len %d, cap %d, \n", arr, len(arr), slice, len(slice), cap(slice))

    slice[0] = 333

    fmt.Printf("arr %v len %d, slice %v  len %d, cap %d, \n", arr, len(arr), slice, len(slice), cap(slice))

    slice = append(slice, 4444)
	slice[0] = 4445
    fmt.Printf("arr %v len %d, slice %v  len %d, cap %d, \n", arr, len(arr), slice, len(slice), cap(slice))

    slice = append(slice, 5555)

    fmt.Printf("arr %v len %d, slice %v  len %d, cap %d, \n", arr, len(arr), slice, len(slice), cap(slice))

    slice[0] = 3133

    fmt.Printf("arr %v len %d, slice %v  len %d, cap %d, \n", arr, len(arr), slice, len(slice), cap(slice))
}