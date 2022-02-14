#!/usr/bin/perl
use strict;
use warnings;

while (<>) {
    s/\b(\d+)0\b/$1/g;
    print
}
