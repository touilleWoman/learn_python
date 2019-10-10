#!/usr/bin/php
<?php
if ($argc > 1)
{
	$str = preg_replace('/  +/', ' ', $argv[1]);
	$str = trim($str);
	$tab = explode(' ', $str, 2);
	$tmp = $tab[0];
	$tab[0] = $tab[1];
	$tab[1] = $tmp;
	echo implode(' ', $tab) . "\n";
}
?>
