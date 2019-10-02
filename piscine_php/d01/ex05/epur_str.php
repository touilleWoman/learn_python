#!/usr/bin/php
<?php
if ($argc == 2)
{
	$str = $argv[1];
	while (strstr($str, '  '))
		$str = str_replace('  ', ' ', $str);
	$pattern = array();
	$replacement = array();
	$pattern[0] = '/ $/';
	$replacement[0] = '';
	$pattern[1] = '/^ /';
	$replacement[1] = '';
	echo preg_replace($pattern, $replacement, $str) . "\n";
}
?>
