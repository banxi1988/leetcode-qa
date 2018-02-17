package main

import "fmt"

func findLUSlength(a string, b string) int {
  aLen := len(a)
  bLen := len(b)
  if aLen > bLen{
	  return aLen
  }else if bLen > aLen{
	  return bLen
  }
  if a == b{
	  return -1
  }
  return aLen
}

func main(){
	fmt.Println("aba,cdc = ",findLUSlength("aba", "cdc"))
	fmt.Println("aba,abc = ",findLUSlength("aba", "abc"))
}