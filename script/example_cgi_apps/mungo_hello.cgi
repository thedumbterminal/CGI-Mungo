#!/usr/bin/perl
use strict;
use warnings;
my $options = {
	'responsePlugin' => 'CGI::Mungo::Response::Raw',
	'checkReferer' => 0
};
my $m = App->new($options);
$m->run();	#do this thing!
#########################################################################################################
##########################################################################################################
package App;
use lib qw(lib ../lib ../../lib);
use strict;
use warnings;
use base qw(CGI::Mungo);
#########################################################################################################
sub handleDefault{
	my $m = shift;
	my $response = $m->getResponse();
	$response->setContent("Hello World");
	return 1;
}