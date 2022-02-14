#!/usr/bin/perl
use strict;
use warnings;

while (<>) {
    print if /\b[1-9]\d*\b/;
}
