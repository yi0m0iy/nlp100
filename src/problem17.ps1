$text = Get-Content ..\data\hightemp.txt
$text|%{($_ -split "\t")[0]}|Sort-Object|Get-Unique
