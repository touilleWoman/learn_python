#!/usr/bin/php
<?php
$i = 0;
foreach ($argv as $value)
{
	if ($i == 0)
		$i++;
	else
		echo "$value\n";
}
?>