#!/bin/sh

install_miniconda()
{
	`
	cd /sgoinfre/goinfre/Perso &&
	mkdir -p '$USER' &&
	chmod 700 '$USER' &&
	cd $USER &&
	curl -o miniconda3.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh &&
	sh miniconda3.sh
	# sh miniconda3.sh -b -p $pwd/miniconda3 && #ligne à verifier
	# echo "" &&
	# echo "à ajouter au .zshrc ou .bashrc: " &&
	export PATH=\"/sgoinfre/goinfre/Perso/$USER/miniconda3/bin:\$PATH\"
	echo "Python has been installed."
	`
}

check_python()
{
	p_version=`python --version`
	if [[ "$p_version" == "Python 3.7.4" ]]; then
		echo "Python is already installed, do you want to reinstall it ?"
				echo "[yes|no]"
				read answer
				if [[  "$answer" == "no" ]]; then
					echo "exit."
					exit
				elif [[ "$answer" == "yes" ]]; then
					`trash /sgoinfre/goinfre/Perso/$USER/miniconda3`
					echo "Python has been removed."
					install_miniconda
				fi
	fi
}

if [ -z "$1"  ]; then
	echo "Empty input! Please type a command."
elif [ "$1" == "install-python" ]; then
	check_python
else
	echo "wrong input"
fi