int main() {

 char *src = EXAMPLE_STR;

 char dest[BUF_SIZE];

 bcopy(src, dest, BUF_SIZE);

 memcpy(dest, src, BUF_SIZE);

}
