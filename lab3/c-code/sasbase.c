#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#include "sasbase.h"

// read / print / println

void ___print_void() {}
void ___println_void() {
    printf("\n");
}

// int

int ___read_int() {
    int x;
    scanf("%d", &x);
    return x;
}

void ___print_void_int(int x) {
    printf("%d", x);
}

void ___println_void_int(int x) {
    printf("%d\n", x);
}

// bool

bool ___read_bool() {
    bool x;
    char input[5];
    scanf("%s", input);
    x = strcmp(input, "true") == 0 ? true : false;
    return x;
}

void ___print_void_bool(bool x) {
    printf("%s", x == true ? "true" : "false");
}

void ___println_void_bool(bool x) {
    printf("%s\n", x == true ? "true" : "false");
}

// long

ll ___read_long() {
    ll x;
    scanf("%lld", &x);
    return x;
}

void ___print_void_long(ll x) {
    printf("%lld", x);
}

void ___println_void_long(ll x) {
    printf("%lld\n", x);
}

// double

double ___read_double() {
    double x;
    scanf("%lf", &x);
    return x;
}

void ___print_void_double(double x) {
    printf("%lf", x);
}

void ___println_void_double(double x) {
    printf("%lf\n", x);
}

// math

// pow

int ___pow_int_int_int(int x, int y) { return pow(x, y); }

ll ___pow_long_int_long(int x, ll y) { return pow(x, y); }

double ___pow_double_int_double(int x, double y) { return pow(x, y); }

ll ___pow_long_long_int(ll x, int y) { return pow(x, y); }

ll ___pow_long_long_long(ll x, ll y) { return pow(x, y); }

double ___pow_double_long_double(ll x, double y) { return pow(x, y); }

double ___pow_double_double_int(double x, int y) { return pow(x, y); }

double ___pow_double_double_long(double x, ll y) { return pow(x, y); }

double ___pow_double_double_double(double x, double y) { return pow(x, y); }

// abs

int ___abs_int_int(int x) {
    return x > 0 ? x : -x;
}

ll ___abs_long_long(ll x) {
    return x > 0 ? x : -x;
}

double ___abs_double_double(double x) {
    return x > 0 ? x : -x;
}

//int main() {
//    printf("%d", ((1 < 2) & (3 > 2)));
//}