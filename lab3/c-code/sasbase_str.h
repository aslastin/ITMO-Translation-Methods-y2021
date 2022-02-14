#ifndef SASBASE_STR_H
#define SASBASE_STR_H

#include <stdio.h>

struct String {
    char* str;
    size_t size;
};

extern const char* INDEX_BOUND_EXCEPTION;
extern const char* RIGHT_BORDER_IS_LESS;

void throw(const char* m, struct String* s);

#endif /* SASBASE_STR_H */
