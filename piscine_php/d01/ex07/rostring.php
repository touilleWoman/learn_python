#!/usr/bin/php
<?php
if ($argc < 2)
	exit();
$str = $argv[1];
$str = preg_replace('/  */', ' ', $str);
$str = trim($str);
$last = preg_split('/^(.*?ll)/', $str);
print_r($last);
echo $str . "\n";
?>