$text = Get-Content ..\data\hightemp.txt

$text|%{($_ -split "\t")[0]}|Out-File -encoding utf8 "..\output\col1.txt"
$text|%{($_ -split "\t")[1]}|Out-File -encoding utf8 "..\output\col2.txt"
