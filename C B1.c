#include <stdio.h>
#include <string.h>

void insecure_function(char *password) {
    char buffer[10];
    strcpy(buffer, password);
}

int main() {
    char password[20];
    printf("Enter your password: ");
    scanf("%s", password);
    insecure_function(password);
    return 0;
}
