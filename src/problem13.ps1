$col1 = Get-Content ..\output\col1.txt -Encoding utf8
$col2 = Get-Content ..\output\col2.txt -Encoding utf8

$mergedCols = @()
foreach ($counter in 1..$col1.length) {
  $mergedLine = $col1[$counter-1], $col2[$counter-1] -join "`t"
  $mergedCols += $mergedLine
}
$mergedCols|Out-File "..\output\merge.txt" -encoding utf8
