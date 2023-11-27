int foo(int a, int b) {
  if (b == 0) {
    a = 1;
  }
  return a / b; // Noncompliant: potential divide-by-zero error
}
