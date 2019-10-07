#!/usr/bin/php
<?php
if ($argc >= 2)
{
	$str = trim($argv[1]);
	$str = preg_replace('/\t/', ' ', $str);
	$str = preg_replace('/  */', ' ', $str);
	echo "$str\n";
}
?>