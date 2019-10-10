<?php
	if (isset($_GET['action']) and isset($_GET['name']))
	{
		if ($_GET['action'] == 'set')
			setcookie($_GET['name'], $_GET['value'], (time() + 3600 * 24));
		elseif ($_GET['action'] == 'get')
			if (isset($_COOKIE[$_GET['name']]))
				echo $_COOKIE[$_GET['name']] . "\n";
		elseif ($_GET['action'] == 'del')
			setcookie($_GET['name'], NULL, time() - 3600*24*12);
	}
?>


//not done