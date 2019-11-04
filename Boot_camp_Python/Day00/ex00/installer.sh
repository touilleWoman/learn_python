#!/bin/sh

if [ -z "$1"  ]; then
	echo "Empty input! Please type a command."
elif [[ "$1" == "intall-python" ]]; then
	if [[ -d /sgoinfre/goinfre/Perso/$USER/miniconda3 ]]; then
		echo "Python is already installed, do you want to reinstall it ?"
		echo "[yes|no]"
		read answer
		if [[  "$answer" == "no" ]]; then
			echo "exit."
			exit
		elif [[ "$answer" == "yes" ]]; then
			echo "Python has been removed."
			echo "Python has been installed."
		fi
	else
		`
		cd /sgoinfre/goinfre/Perso &&
		mkdir -p '$USERNAME' &&
		chmod 700 '$USERNAME' &&
		cd $USERNAME &&
		curl -o miniconda3.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh &&
		sh miniconda3.sh
		# sh miniconda3.sh -b -p $pwd/miniconda3 && #ligne à verifier
		# echo "" &&
		# echo "à ajouter au .zshrc ou .bashrc: " &&
		export PATH=\"/sgoinfre/goinfre/Perso/$USERNAME/miniconda3/bin:\$PATH\"
		echo "Python has been installed."
		`
	fi
else
	echo "wrong input"
fi