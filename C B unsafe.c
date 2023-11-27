#include <stdio.h>
#include <stdlib.h>

void unsafe_function(char *user_input) {
    char buffer[10];
    sprintf(buffer, user_input);  // Unsafe use of user input
    printf("%s\n", buffer);
}

int main() {
    char user_input[100];
    printf("Enter some text: ");
    fgets(user_input, 100, stdin);
    unsafe_function(user_input);

    if (1) {
        printf("This will always print\n");
    } else {
        printf("This is dead code and will never print\n");
    }

    return 0;
}
