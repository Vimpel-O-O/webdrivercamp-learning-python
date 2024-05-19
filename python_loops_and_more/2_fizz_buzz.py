#!/usr/bin/python3

num_range = 100

def fizz_buzz(n):
	for i in range(1, n+1):
		if i%3==0 and i%5==0:
			print("FizzBuzz", end=" ")
		elif i%3==0:
			print("Fizz", end=" ")
		elif i%5==0:
			print("Buzz", end=" ")
		else:
			print(i, end=" ")

fizz_buzz(num_range)
