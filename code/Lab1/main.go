package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var englishAlphabet []int32

func input(option *int, k1 *int, k2 *string, line *string) {
	fmt.Print("What operation do you want to perform? 1. Enc / 2. Dec - ")
	_, _ = fmt.Scanln(option)

	fmt.Print("What is the key1 value? - ")
	_, _ = fmt.Scanln(k1)

	in := bufio.NewReader(os.Stdin)

	fmt.Print("What is the key2 value? - ")
	*k2, _ = in.ReadString('\n')

	fmt.Print("What is the message/cryptogram? ('A' -> 'Z', 'a' -> 'z') : ")
	*line, _ = in.ReadString('\n')
}

func validate(line string, alphabet []int32) bool {
	if len(line) == 0 {
		return true
	}

	var verdict bool

	for _, charL := range line {
		verdict = false

		for _, charA := range alphabet {
			if charL == charA {
				verdict = true
				break
			}
		}

		if verdict == false {
			break
		}
	}

	return verdict
}

func format(line string) string {
	var newLine string

	for _, char := range line {
		if char != ' ' {
			newLine += string(char)
		}
	}

	newLine = newLine[0 : len(newLine)-1]

	return newLine
}

func encdec(line string, key int, operation int, alphabet []int32) string {
	var finalMsg string

	var searchAlphabet []int32
	var getAlphabet []int32

	if operation == 1 {
		searchAlphabet = englishAlphabet
		getAlphabet = alphabet
	} else {
		searchAlphabet = alphabet
		getAlphabet = englishAlphabet
	}

	for _, charL := range line {
		var newCharIndex int

		for index, charA := range searchAlphabet {
			if charL == charA {
				if operation == 1 {
					newCharIndex = (index + key) % len(searchAlphabet)
				} else {
					newCharIndex = (index - key) % len(searchAlphabet)
					if newCharIndex < 0 {
						newCharIndex = len(searchAlphabet) + newCharIndex
					}
				}
				break
			}
		}

		finalMsg += string(getAlphabet[newCharIndex])
	}

	return finalMsg
}

func permuteAlphabet(key2 string, alphabet []int32) []int32 {
	var newAlphabet []int32

	for _, char := range key2 {
		newAlphabet = append(newAlphabet, char)
	}

	for _, char := range alphabet {
		newAlphabet = append(newAlphabet, char)
	}

	edited := true

	for edited {
		edited = false

		for i, charI := range newAlphabet[:len(newAlphabet)-1] {
			for j, charJ := range newAlphabet[i+1:] {
				if charI == charJ {
					newAlphabet = append(newAlphabet[:j+i+1], newAlphabet[j+i+2:]...)
					edited = true

					break
				}
			}

			if edited {
				break
			}
		}
	}

	return newAlphabet
}

func main() {
	for char := 'A'; char <= 'Z'; char++ {
		englishAlphabet = append(englishAlphabet, char)
	}

	alphabet := englishAlphabet

	var option, k1 int
	var k2, line string

	input(&option, &k1, &k2, &line)

	line = format(strings.ToUpper(line))

	if len(k2) > 0 {
		k2 = format(strings.ToUpper(k2))
	}

	if !validate(line, alphabet) || !validate(k2, alphabet) {
		fmt.Println("==================================")
		fmt.Println("ERROR: Unknown character detected!")
		fmt.Println("==================================")

		return
	}

	if len(k2) > 0 {
		alphabet = permuteAlphabet(k2, alphabet)
	}

	fmt.Println("----------------------------------")
	fmt.Println(encdec(line, k1, option, alphabet))
}
