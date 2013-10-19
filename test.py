#!/usr/bin/python

"""
You are given an array of N integers. At each step:

1) You can increase the value of any cell in the array by 1 or

2) You can decrease the value of any cell in the array by 1.

What are the minimum number of steps required to make the sequence non-decreasing(b1<=b2<=...<=bn, bi represent an element in the sequence).

Input:

First line represent the number of test cases. Each test case contains 2 lines,First line for a single integer N. The following line contains N integers each, the elements of the sequence.

Output:

Output one integer, the minimum number of steps required to achieve the goal, for each test case followed by an end line.

Sample Input
  5 
  3 2 0 2 5 
  3 
  2 2 1 
  4 
  0 0 0 0
Sample Output
  3 
  1 
  0

"""

def min_steps(n, sequence):
  steps = 0
  for i in range(n):
    if i < n-1 and sequence[i] > sequence[i+1]:
      steps += sequence[i] - sequence[i+1]
  print str(sequence) + ':' + str(steps)
  return steps

def test_min_steps():
  if min_steps(5, [3,2,0,2,5]) != 3:
    print "Test 1 failed"
  if min_steps(3, [2,2,1]) != 1:
    print "Test 2 failed"
  if min_steps(4, [0,0,0,0]) != 0:
    print "Test 3 failed"
  min_steps(6, [2,10,1,5,2,1])

test_min_steps()