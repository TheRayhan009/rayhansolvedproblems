#include <iostream>
#include <string>
using namespace std;

int main() {
    string operation;
    double num1, num2;

    cout << "Simple Calculator" << endl;
    cout << "Enter operation (e.g., + 5 3) or type 'exit' to quit:" << endl;

    while (true) {
        cin >> operation;
        if (operation == "exit") {
            break;
        }
        cin >> num1 >> num2;

        if (operation == "+") {
            cout << num1 + num2 << endl;
        } else if (operation == "-") {
            cout << num1 - num2 << endl;
        } else if (operation == "*") {
            cout << num1 * num2 << endl;
        } else if (operation == "/") {
            if (num2 != 0) {
                cout << num1 / num2 << endl;
            } else {
                cout << "Error: Division by zero" << endl;
            }
        } else {
            cout << "Invalid operation" << endl;
        }
    }

    return 0;
}
