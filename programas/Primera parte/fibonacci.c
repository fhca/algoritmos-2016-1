#include<stdio.h>

int main(){
    unsigned long a = 1,
         b = 1,
         c = a + b;
    printf("%lu\n%lu\n", a, b);
    while(c < 1e9) {
        printf("%lu\n", c);
        a = b;
        b = c;
        c = a + b;
    }
    return 0;
}
