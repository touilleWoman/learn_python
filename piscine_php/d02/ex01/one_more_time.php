#!/usr/bin/php
<?php
function get_year($str)
{
	preg_match('/\d{4}/', $str, $year);
	return $year[0];
}

function get_month($str)
{
	preg_match('/((j|J)anvier|(f|F)(e|é)vrier|(m|M)ars|(a|A)vril|(m|M)ai|(j|J)uin|(J|j)uillet|(a|A)o(û|u)t|(s|S)eptembre|(o|O)ctobre|(N|n)ovembre|(d|D)(e|é)cembre)/', $str, $month);
	$i = 0;
	if($month[0] == 'janvier')
		return 1;
	elseif($month[0] == 'fevrier')
		return 2;
	elseif($month[0] == 'mars')
		return 3;
	elseif($month[0] == 'avril')
		return 4;
	elseif($month[0] == 'mai')
		return 5;
	elseif($month[0] == 'juin')
		return 6;
	elseif($month[0] == 'juillet')
		return 7;
	elseif($month[0] == 'aout')
		return 8;
	elseif($month[0] == 'septembre')
		return 9;
	elseif($month[0] == 'octobre')
		return 10;
	elseif($month[0] == 'novembre')
		return 11;
	elseif($month[0] == 'decembre')
		return 12;
}

function get_hour($str)
{
	preg_match('/ \d{2}:/', $str, $hour);
	$ret = substr($hour[0], 1, 2);
	return $ret;
}

function get_minute($str)
{
	preg_match('/:\d{2}:/', $str, $minute);
	$ret = substr($minute[0], 1, 2);
	return $ret;
}

function get_second($str)
{
	preg_match('/:\d{2}$/', $str, $second);
	$ret = substr($second[0], 1, 2);
	return $ret;
}

function get_day($str)
{
	preg_match('/ \d{1,2} /', $str, $day);
	$len = strlen($day[0]);
	if ($len == 4)
		$ret = substr($day[0], 1, 2);
	elseif ($len == 3)
		$ret = substr($day[0], 1, 1);
	return $ret;
}

function take_off_accents($str)
{
	$accents = array('û', 'é');
	$replace = array('u', 'e');
	$new_str = str_replace($accents, $replace, $str);
	return $new_str;
}

if ($argc >=2)
{
	if (preg_match('/^(((l|L)undi)|((m|M)ardi)|((m|M)ercredi)|((j|J)eudi)|((v|V)endredi)|((s|S)amedi)|((d|D)imanche)) \d{1,2} ((j|J)anvier|(f|F)(e|é)vrier|(m|M)ars|(a|A)vril|(m|M)ai|(j|J)uin|(J|j)uillet|(a|A)o(û|u)t|(s|S)eptembre|(o|O)ctobre|(N|n)ovembre|(d|D)(e|é)cembre) \d{4} \d{2}:\d{2}:\d{2}$/', $argv[1]))
	{
		$str = strtolower($argv[1]);
		$str = take_off_accents($str);
		$year = get_year($str);
		$day = get_day($str);
		$month = get_month($str);
		$minute = get_minute($str);
		$hour = get_hour($str);
		$second = get_second($str);
		echo mktime($hour, $minute, $second, $month, $day, $year) . "\n";
	}
	else
		echo "Wrong Format\n";
}
?>
