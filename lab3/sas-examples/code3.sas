n = read<int>();

for@ (a <- [1,6..n], b <- [1..a], a + b <= 100) {
    println(a + b);
}
