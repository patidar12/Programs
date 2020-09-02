'''
Print all subsequence of a string

Input:
abc

Output:

c
b
bc
a
ac
ab
abc

# cpp
#Using output Array

#include <iostream>
using namespace std;

int subs(string input, string output[]) {
	if (input.empty()) {
		output[0] = "";
		return 1;
	}

	string smallString = input.substr(1);
	int smallOutputSize = subs(smallString, output);
	for (int i = 0; i < smallOutputSize; i++) {
		output[i + smallOutputSize] = input[0] + output[i];
	}
	return 2 * smallOutputSize;
}

int main() {
	string input;
	cin >> input;
	string* output = new string[1000];
	int count = subs(input, output);
	for (int i = 0; i < count; i++) {
		cout << output[i] << endl;
	}
}


'''
# Python
def subs(string,output):
    if(len(string) == 0):
        output[0] = ''
        return 1
    smallSubsSize = subs(string[1:],output)
    for i in range(0,smallSubsSize):
        output[i+smallSubsSize] = string[0] + output[i]
    return 2*smallSubsSize

string = input()
output = [None]*(2**len(string))
count = subs(string,output)
for i in range(count):
    print(output[i])
