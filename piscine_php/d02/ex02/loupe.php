#!/usr/bin/php
<?php

function convert_maj($matches)
{
	$matches[0] = preg_replace_callback('/>.*?</', strtoupper($matches[0]), subject)
	preg_match_all('/title=/', replacement, subject)
	return strtoupper($matches);
}

if ($argc > 1)
{
	$str = file_get_contents($argv[1]);
	$pattern = '/<a href=.*?>.*?<\/a>/';
	echo preg_replace_callback($pattern, "convert_maj", $str);
}

?>
not done???