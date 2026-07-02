package main

import "fmt"

func main() {
	field := [32][32]string{}
	for i, _ := range field {
		for j := range field[i] {
			field[i][j] = " "
		}
	}
	field[2][3] = "@"
	for _, v:= range field{
		fmt.Println(v)
	}
}