# n(行ごとに)分割
Param(
  [Parameter(Mandatory=$True,
    position=1)]
  [Alias('n')]
  [int]$Number
)

function Generate-Suffix {
  Param(
    [Parameter(Mandatory=$True,
      position=1)]
    [int]$N,

    [string[]]$CharList
  )
  if ($Null -eq $CharList) {
    $CharList = 97..122|%{[char]$_}
  }

  if ($N -eq 1) {
    return $CharList
  } elseif($N -gt 1) {
    return $(foreach ($char in $CharList) {
      foreach ($suf in Generate-Suffix ($N - 1) -CharList $CharList) {
        $char + $suf
      }
    })
  } else {
    return
  }
}

$text = Get-Content "..\data\hightemp.txt"
$sufList = Generate-Suffix(2)
$counter = 0
$splitList = while($Number*$counter -lt $text.length) {
  @{number = $Number*$counter; suffix = $sufList[$counter]}
  $counter++
}

foreach ($sp in $splitList) {
  $sublist = $text[$sp.number..($sp.number + $Number - 1)]
  $sublist|Out-File ("..\output\hightemp.split." + $sp.suffix) -encoding utf8
}
