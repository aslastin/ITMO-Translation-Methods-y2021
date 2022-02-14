#!/usr/bin/perl
use strict;
use warnings;

while (<>) {
    print if /[xyz]\w{5,17}[xyz]/i;
}
