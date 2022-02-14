f@ f(a, b, c) {
    r@ a^b^c;
}

f@ g(a) {
    r@ |a|;
}

a, b, c = read<int>(), read<int>(), read<int>();

println(f<int>(a, b, c));
println(f<int>(a, b, g<int>(c)));

// Разумеется есть форы

if@ (10 > a > 5) {
    println(a^3);
}

ifelse@ (b > c > -5) { println(b^2); | println(b^3); }


/*
if@ (5 > 5) {
}

f@ g() {}


*/

