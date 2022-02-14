#!/usr/bin/perl
use strict;
use warnings;

while (<>) {
    s/\b(\w+)\b(.*?)\b(\w+)\b/$3$2$1/;
    print
}
