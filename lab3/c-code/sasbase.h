#ifndef SASBASE_H
#define SASBASE_H

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

typedef long long ll;

void ___print_void();
void ___println_void();

int ___read_int();
void ___print_void_int(int x);
void ___println_void_int(int x);

bool ___read_bool();
void ___print_void_bool(bool x);
void ___println_void_bool(bool x);

ll ___read_long();
void ___print_void_long(ll x);
void ___println_void_long(ll x);

double ___read_double();
void ___print_void_double(double x);
void ___println_void_double(double x);

int ___pow_int_int_int(int x, int y);
ll ___pow_long_int_long(int x, ll y);
double ___pow_double_int_double(int x, double y);
ll ___pow_long_long_int(ll x, int y);
ll ___pow_long_long_long(ll x, ll y);
double ___pow_double_long_double(ll x, double y);
double ___pow_double_double_int(double x, int y);
double ___pow_double_double_long(double x, ll y);
double ___pow_double_double_double(double x, double y);

int ___abs_int_int(int x);
ll ___abs_long_long(ll x);
double ___abs_double_double(double x);

#endif //SASBASE_H
