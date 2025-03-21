#include <stdio.h>

int fibonaci(int n);

int main()
{
    int n = 10;
    fibonaci(n);
    return 0;
}

int fibonaci(int n) {
    if (n < 2) {
        return n;
    }
    return fibonaci(n - 1) + fibonaci(n - 2);
}