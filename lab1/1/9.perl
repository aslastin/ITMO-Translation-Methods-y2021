#!/usr/bin/perl
use strict;
use warnings;

while (<>) {
    next if (/^\ +/ || /\ +$/);
    print;
}
