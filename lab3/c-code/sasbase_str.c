#include <stdlib.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include "sasbase_str.h"

//#include <stdbool.h>
#define isCompatible(x, type) _Generic(x, type: true, default: false)
//isCompatible(s1.str, char)

#include "sasbase_str.h"

const char* INDEX_BOUND_EXCEPTION = "index out of bound in: ";

const char* RIGHT_BORDER_IS_LESS = "right border is less than left: ";

void throw(const char* m, struct String* s) {
    char* message = malloc((strlen(m) + s->size) * sizeof(char));
    fprintf(stderr, "%s\n", strcat(strcat(message, m), s->str));
    exit(1);
}



// str = “Hello, man” -> str = newString(“Hello, man”)
// str = str1 -> str = str1
struct String newString(char* str) {
    size_t size = strlen(str);

    char* s = malloc((size + 1) * sizeof(char));
    memcpy(s, str, size + 1);

    struct String r = {s, size};

    return r;
}


// ind(& s1, 1)
struct String ind(struct String *s, size_t index) {
    if (index >= s->size) {
        throw(INDEX_BOUND_EXCEPTION, s);
    }

    char* res = malloc(2 * sizeof(char));
    res[0] = s->str[index];
    res[1] = '\0';

    struct String r = {res, 1};

    return r;
}

struct String slice(struct String *s, size_t ind_start, size_t ind_end) {
    if (ind_start >= s->size || ind_end >= s->size) {
        throw(INDEX_BOUND_EXCEPTION, s);
    }

    if (ind_end < ind_start) {
        throw(RIGHT_BORDER_IS_LESS, s);
    }

    size_t slice_size = ind_end - ind_start;
    char* tmp = s->str;

    for (size_t i = 0; i < ind_start; i++) {
        tmp++;
    }

    char* str = malloc((slice_size + 1) * sizeof(char));
    memcpy(str, tmp, slice_size * sizeof(char));
    str[slice_size] = '\0';

    struct String res = {str, slice_size};

    return res;
}

void print(struct String* s) {
    printf("%s", s->str);
}

void println(struct String* s) {
    printf("%s\n", s->str);
}

void failure(char *arr) {
    free(arr);
    exit(1);
}

struct String readStr(void) {
    const size_t CHUNK_SIZE = 8;
    size_t arrSize = CHUNK_SIZE;
    char *arr = malloc(arrSize);

    if(!arr) {
        fprintf(stderr, "Initial allocation failed.\n");
        failure(arr);
    }

    // One past the end of the array
    // (next insertion position)
    size_t arrEnd = 0u;

    for(char c = '\0'; c != '\n';) {

        if(scanf("%c", &c) != 1) {
            fprintf(stderr, "Reading character %zu failed.\n", arrEnd);
            failure(arr);
        }

        // No more room, grow the array
        // (-1) takes into account the
        // nul terminator.
        if(arrEnd == arrSize - 1) {
            arrSize += CHUNK_SIZE;
            char *newArr = realloc(arr, arrSize);

            if(!newArr) {
                fprintf(stderr, "Reallocation failed.\n");
                failure(arr);
            }

            arr = newArr;
        }

        // Append the character and
        // advance the end index
        arr[arrEnd++] = c;
    }
    // Nul-terminate the array
    arr[arrEnd] = '\0'; // ++

    // Done !

    struct String r = {arr, arrEnd - 1};

    return r;
}

long long cast_int_long(int val) {
    return (long long) val;
}

long long cast_intp_long(int* val) {
    return (long long) *val;
}

struct String cast(char* format, int val) {
//    void* value;
//    if (strcmp(format, "%F") == 0) {
//        double value = *((double*) val);
//    } else if (strcmp(format, "%d") == 0) {
//        int value = *((int*) val);
//    } else if (strcmp(format, "%ll") == 0) {
//        long long value = *((long long*) val);
//    } else if (strcmp(format, "bool") == 0) {
//        bool t = *((bool*) val);
//        format = "%s";
//        if (t) {
//            char* value = "true";
//        } else {
//            char* value = "false";
//        }
//    } else {
//        struct String s = {"", 0};
//        char m[] = "incorrect argument \"format\"";
//        throw(m, &s);
//    }

//    if (isCompatible(value, int)) {
//        printf("%s\n", "yes");
//    }

    int len = snprintf(NULL, 0, format, val);
    char* res = malloc((len + 1) * sizeof(char));
    sprintf(res, format, val);

    return (struct String) {res, len};
}

char *my_getline(int init_size) {
    char *line = malloc(init_size), *linep = line;
    size_t lenmax = init_size, len = lenmax;
    int c;

    if (line == NULL)
        return NULL;

    for (;;) {
        c = fgetc(stdin);
        if (c == EOF)
            break;

        if (--len == 0) {
            len = lenmax;
            char *linen = realloc(linep, lenmax *= 2);

            if (linen == NULL) {
                free(linep);
                return NULL;
            }
            line = linen + (line - linep);
            linep = linen;
        }

        if ((*line++ = c) == '\n')
            break;
    }
    *line = '\0';
    return linep;
}