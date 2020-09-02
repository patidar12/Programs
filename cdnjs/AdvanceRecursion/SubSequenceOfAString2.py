'''
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

# using output string
# cpp


#include <iostream>
using namespace std;

void print_subs(string input, string output) {
	if (input.length() == 0) {
		cout << output << endl;
		return;
	}

	print_subs(input.substr(1), output);
	print_subs(input.substr(1), output + input[0]);
}

int main() {
	string input;
	cin >> input;
	string output = "";
	print_subs(input, output);
}

'''

# python
def subs(string,output):
    if(len(string) == 0):
        print(output)
        return
    subs(string[1:],output)
    subs(string[1:],output+string[0])

string = input()
output = ""
count = subs(string,output)
