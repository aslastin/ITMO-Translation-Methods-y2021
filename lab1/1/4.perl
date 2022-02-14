#!/usr/bin/perl
use strict;
use warnings;

while (<>) {
    print if /z\w{3}z/i;
}
