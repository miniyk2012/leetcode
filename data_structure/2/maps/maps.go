package main

import (
	"fmt"
	"strings"
)

type Vertex struct {
	Lat, Long float64
	b [4]int
}

var x Vertex = Vertex {
	Lat: 10.3, Long: 100.4}

func main() {
	fmt.Println(x)
	fmt.Printf("Fields are: %q", strings.Fields("  foo bar  baz   "))
}
