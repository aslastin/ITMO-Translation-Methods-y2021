#!/usr/bin/perl
use strict;
use warnings;

while (<>) {    
    print if /\b(\w+)\g1\b/;
}
