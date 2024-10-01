#include <iostream>
#include <string>

int main(void) {
    std::string word, sig, oldsig = "";
    int linenum = 0;
    while (std::cin >> sig >> word) {
        if (oldsig != sig && linenum > 0) {
            std::cout << std::endl;
        }
        std::cout << word << " ";
        oldsig = sig;
        linenum++;
    }
    std::cout << std::endl;
    return 0;
}