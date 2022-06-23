use strict;

my $stGFF3=$ARGV[0];	###	NCBI/Phytophthora_parasitica_INRA-310/GCF_000247585.1_PP_INRA-310_V2_genomic.gff

open(DATA, "$stGFF3");
my %stList;

while(my $stLine = <DATA>)
{
	chomp($stLine);
	my @stInfo=split(/\t/,$stLine);
	if($stInfo[2] eq "mRNA")
	{
		$stInfo[8] =~ s/(^ID=[^\;]+);.+/$1/g;
		my $stRNA=join("\t",@stInfo);
		$stList{$stInfo[8]}=$stList{$stInfo[8]}."$stRNA\n";
	}
	elsif($stInfo[2] eq "CDS")
	{
		my $stParent="";
		if($stInfo[8] =~ /Parent=([^\;]+)/)
		{
			$stParent="ID=".$1;
			next if($stParent !~ /rna/);
		}
		if($stInfo[8] =~ /protein_id=([^\;]+)/)
		{
			$stInfo[8]="ID=".$1;
			my $stCDS=join("\t",@stInfo);
			$stList{$stParent}=$stList{$stParent}."$stCDS\n";
		}
		else
		{
			print "Error	$stInfo[8]\n";
			exit;
		}
	}
}
close DATA;

foreach my $stKey(sort{($a =~ /rna([0-9]+)/)[0] <=> ($b =~ /rna([0-9]+)/)[0]}keys%stList)
{
	my @stInfo=split(/\n/,$stList{$stKey});
	@stInfo=sort{	($b =~ /^[^\s]+	[^\s]+	([^\s]+)	[^\s]+	/)[0] cmp ($a =~ /^[^\s]+	[^\s]+	([^\s]+)	[^\s]+	/)[0] ||
			($a =~ /^[^\s]+	[^\s]+	[^\s]+	([^\s]+)	/)[0] <=> ($b =~ /^[^\s]+	[^\s]+	[^\s]+	([^\s]+)	/)[0]
	}@stInfo;
	my @stID=split(/\t/,$stInfo[$#stInfo]);
	for(my $i=0; $i<@stInfo; $i++)
	{
		my @stFinal=split(/\t/,$stInfo[$i]);
		if($i == 0)
		{
			$stFinal[8]=$stID[$#stID];
			my $stFinal=join("\t",@stFinal);
			my $stGene=$stFinal;
			$stGene =~ s/	mRNA	/	gene	/;
			print "$stGene\n$stFinal\n";
		}
		else
		{
			$stFinal[8]=$stID[$#stID];
			my $stFinal=join("\t",@stFinal);
			my $stExon=$stFinal;
			$stExon =~ s/	CDS	/	exon	/;
			print "$stExon\n$stFinal\n";
		}
	}
	print "\n";
}
