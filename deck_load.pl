use strict;
use warnings;

my $filename = $ARGV[0];

open my $fh, "<$filename";




print("CREATE (deck:Deck {name:'$filename'})\n");
my $c = 0;
while (my $line = <$fh>) {
	if ($line =~ /([0-9]+) (.*)$/) {
		$c++;
		my $name = "'$2'";
		my $count = $1;

		print("CREATE (card$c:Card {name:$name})\n");
		print("CREATE (card$c)-[:IN {count:$count}]->(deck)\n");
	}
}
