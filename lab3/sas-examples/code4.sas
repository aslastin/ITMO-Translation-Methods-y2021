f@ fac(n) {
    ifelse@ (n <= 0) { r@ 1; | r@ n * fac<int>(n - 1); }
}

for@ (i <- [1..10)) {
    println(fac<int>(i));
}
println();

// Еще крутая фича - учитываем скоупы

a = 2.5;
b = 7.5;
println(a + b);

if@ (true or false) {
    b = 2.5;
    println(a + b);
    if@ (true and true)  {
        b = true;
        println(b);
    }
    println(b);
    b = 100;
}

println(a + b);

a, b, c, d = read<int>(), read<int>(), read<int>(), read<int>();
println(a <= b > c < d > 25);

println(a > b);


a = 1;
if@ (true) {
    a = 2.5;
}
println(a);
