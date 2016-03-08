""" You have a record of NN students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer NN followed by the names and marks for NN students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer NN, the number of students. The next NN lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Constraints
2 <= N <= 10
0 <= Marks <= 100

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output

56.00

Concept

A dictionary is a data type which stores values in pairs. For each element in the dictionary, there is a unique key that points to a value. A dictionary is mutable. It can be changed.
For example:

>> a = {'one': 1} # Here 'one' is the key.  

Note: The key of a dictionary is immutable. We cannot use a list as a key because a list is mutable.

>> a['two'] = 2 # Adds key 'two' which points to 2
>> a['one']
1  
>> if ('three' in a):
      # To check whether a certain string exist as a key in the dictionary  
..    print a['three']
.. else:  
..    print "Three not there"
Three not there
>> del a['one']
# Deletes index 'one' and the value associated with it  
>> a
{'two': 2}

Note: A dictionary is unordered. So, only use the keys to navigate through the dictionary. """

#submissions
# Enter your code here. Read input from STDIN. Print output to STDOUT

#input
N = int(raw_input())

#dictionary
S = {}

for i in range(N):
	stu = raw_input()
	p_stu = stu.split()
	S[p_stu[0]] = " ".join(str(x) for x in p_stu[1:])

#sesuai nama
pil_nama = str(raw_input())
for key,values in S.items():
	if key == pil_nama:
		nilai = values.split()
		rata = (sum(float(i) for i in nilai) / len(nilai))
		print '{:.2f}'.format(rata)
