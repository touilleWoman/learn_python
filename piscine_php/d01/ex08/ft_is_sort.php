#!/usr/bin/php
<?php
function ft_is_sort($tab)
{
	$i = 0;
	$sorted = $tab;
	sort($sorted);
	foreach ($sorted as $value)
	{
		if ($value != $tab[$i])
			return FALSE;
		$i++;
	}
	return TRUE;
}
?>