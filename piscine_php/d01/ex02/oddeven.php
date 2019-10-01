#!/usr/bin/php
<?php
while (!(feof(STDIN)))
{
	echo "Entrez un nombre: ";
	$nb = trim(fgets(STDIN));
	if (is_numeric($nb))
	{
		if ($nb % 2 == 0)
		{
			echo "Le chiffre $nb est Pair\n";
		}
		else
		{
			echo "Le chiffre $nb est Impair\n";
		}
	}
	else
	{
		echo "'$nb' n'est pas un chiffre\n";
	}
}
?>