#!/usr/bin/perl
use strict;
use warnings;

my $flg = 0;
while (<>) {
    s/<.*?>//g;
    unless (/^\ *$/) {
        /^\ *(.+?)\ *$/;
        my $a = $1;
        $a =~ s/\ +/\ /g;
        if ($flg != 0) {
            print "\n";
        }
        if ($flg == 1) {
            print "\n";
        }
        $flg = 2;
        print $a;
    } elsif ($flg == 2) {
        $flg = 1;
    }
}
