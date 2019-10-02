#!/usr/bin/php
<?php
if ($argc == 2)
{
	$str = $argv[1];
	$str = preg_replace('/  */', ' ', $str);
	$str = preg_replace('/ $/', '', $str);
	$str = preg_replace('/^ /', '', $str);
	echo "$str\n";
}
?>
