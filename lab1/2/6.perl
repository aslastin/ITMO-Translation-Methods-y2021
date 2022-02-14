#!/usr/bin/perl
use strict;
use warnings;

while (<>) {
    s/(\w)\g1/$1/g;
    print
}
