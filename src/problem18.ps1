Get-Content "..\data\hightemp.txt"|Sort-Object {($_ -split "`t")[2]} -Descending
