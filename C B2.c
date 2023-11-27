#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("example.txt", "r");
    if (file == NULL) {
        printf("Cannot open file\n");
        return 1;
    }
    // ... read from file ...
    fclose(file);  // Close the file when you're done with it
    return 0;
}
