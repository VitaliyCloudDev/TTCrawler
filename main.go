package main

import "fmt"

func createField() [32][32]string {
	field := [32][32]string{}
	for i, _ := range field {
		for j := range field[i] {
			field[i][j] = " "
		}
	}
	return field
}

func renderScreen(field [32][32]string) {
	for _, v := range field {
		fmt.Println(v)
	}
}

func main() {
	field := createField()
	field[2][3] = "@"
	for i := range 10 {
		field[i][i] = "z"
		renderScreen(field)
	}
}

