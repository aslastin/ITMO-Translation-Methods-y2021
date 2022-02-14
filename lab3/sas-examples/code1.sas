// В языке есть динамическая типизация

b, c = |2+2*-2|, 3^3;
println(b);
println(c);
println();

b, c = -2^2^2+|-1|, true;
println(b);
println(c);
println();

cnst@ a = -b + c;
println(a);

// Определеяем функцию
f@  f(a, b, c) {
    r@ b < a > c;
}
println(f<bool>(a, b, c));

// Тип функций выводится из аргументов
// (однако надо указывать возвращаемое значение)
f@ eq(a, b, c, d) {
    r@ a == b == c == d;
}

b, c, d = 1, 1, 1L;
println(eq<bool>(a, b, c, d));

b, c, d = a, a, a;
println(eq<bool>(a, b, c, d));
