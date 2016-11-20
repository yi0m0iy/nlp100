if ($args.length) {
  (Get-Content ..\data\hightemp.txt)[-$args[0]..-1]
}
