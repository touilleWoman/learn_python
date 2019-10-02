#!/usr/bin/php
<?php
if ($argc == 1)
	exit();
$i = 1;
$tab = array();
while ($argv[$i])
{
	$tab =array_merge($tab, explode(" ", $argv[$i]));
	$i++;
}
sort($tab);
foreach ($tab as $value)
{
	echo "$value\n";
}
?>