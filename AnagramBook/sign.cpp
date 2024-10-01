#include <iostream>
#include <string>
#include <algorithm>

#define WORDMAX 100

int charcomp(char x, char y) {
    return x < y;
}

int main(void) {
    std::string word, sig;
    while (std::cin >> word) {
        sig = word;
        std::sort(sig.begin(), sig.end(), charcomp);
        std::cout << sig << " " << word << std::endl;
    }
    return 0;
}