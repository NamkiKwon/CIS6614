void f(int i, int j);

void g() {
  int i = 0;
  f(++i, ++i); // Noncompliant, the call could either be f(1,2) or f(2,1) (since C++17) or undefined behavior (before C++17)
}
