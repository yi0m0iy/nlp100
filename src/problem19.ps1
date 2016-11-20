$col1 = Get-Content "..\data\hightemp.txt"|%{($_ -split "`t")[0]}
$uniqWords = @{}
$col1|Sort-Object|Get-Unique|%{$uniqWords.Add($_, ($col1 -eq $_).count)}
$uniqWords.GetEnumerator()|Sort-Object Value -descending|%{$_.Name + " " + $_.Value}
