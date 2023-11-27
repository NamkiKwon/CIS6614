int volatile f(int volatile i); // Noncompliant, both for the return type and the parameter

void g() {
  auto volatile [a, b] = getPair(); // Noncompliant
}
