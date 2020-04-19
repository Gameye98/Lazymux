
makedeb() {
# Usage: makedeb
echo -e "[makedeb] program running..."
subdir=("bin" "etc" "include" "lib" "libexec" "share" "src" "tmp" "var")
printf "[makedeb] check folder... "
if test ! -d ${HOME}/makedeb; then
	mkdir ${HOME}/makedeb
fi
echo -e "ok"
read -p "[makedeb] package name: " package_name
read -p "[makedeb] version code: " version_code
project_folder="${package_name}_${version_code}_all"
if test -d ${HOME}/makedeb/${project_folder}; then
	echo -e "[makedeb-${package_name}] project exists: ${HOME}/makedeb/${project_folder}"
	exit
else
	echo -e "[makedeb-${package_name}] creating project: ${HOME}/makedeb/${project_folder}"
	mkdir ${HOME}/makedeb/${project_folder}
fi
mkdir ${HOME}/makedeb/${project_folder}/DEBIAN
mkdir -p ${HOME}/makedeb/${project_folder}${PREFIX}
for dir in ${subdir[@]}; do
	read -p "[makedeb-${package_name}] mkdir ${dir}? [Y] " mkdir_subdir
	if [[ "${mkdir_subdir}" == "Y" || "${mkdir_subdir}" == "y" ]]; then
		mkdir ${HOME}/makedeb/${project_folder}${PREFIX}/${dir}
	elif [[ "${mkdir_subdir}" == "done" ]]; then
		break
	fi
done
echo -e "[makedeb-${package_name}] type \"done\" when you're done moving file"
while true; do
	read -p "[makedeb-${package_name}] copy file: " copy_file
	read -p "[makedeb-${package_name}] place them onto ( $(ls $PREFIX | tr '\n' ' ')): " filedest
	if test -f ${copy_file}; then
		cp ${copy_file} ${HOME}/makedeb/${project_folder}${PREFIX}/${filedest}
	elif [[ "${copy_file}" == "done" ]]; then
		cp ${copy_file} ${HOME}/makedeb/${project_folder}${PREFIX}/${filedest}
		break
	else
		echo -e "[makedeb-${package_name}] file not exists: ${copy_file}"
	fi
done
file_control=$(cat <<DOCUMENT
Package: ${package_name}
Version: ${version_code}-stable
Architecture: all
Homepages: http://example.com
Maintainer: YOURNAME <youremail>
Depends: python2
Installed-Size: 100 KB
Description: DESCRIPTION_OF_THE_PACKAGE
DOCUMENT
)
file_postinst=$(cat <<DOCUMENT
#!/data/data/com.termux/files/usr/sh
# write your command, command execute when user install the package

DOCUMENT
)
file_prerm=$(cat <<DOCUMENT
#!/data/data/com.termux/files/usr/sh
# write your command, command execute when user remove the package

DOCUMENT
)
printf "${file_control}\n" > ${HOME}/makedeb/${project_folder}/DEBIAN/control
read -p "[makedeb-${package_name}] add DEBIAN/postinst? [Y] " postinst_add
read -p "[makedeb-${package_name}] add DEBIAN/prerm? [Y] " prerm_add
if [[ "${postinst_add}" == "Y" || "${postinst_add}" == "y" ]]; then
	printf "${file_postinst}\n" > ${HOME}/makedeb/${project_folder}/DEBIAN/postinst
	nvim ${HOME}/makedeb/${project_folder}/DEBIAN/postinst
fi
if [[ "${prerm_add}" == "Y" || "${prerm_add}" == "y" ]]; then
	printf "${file_prerm}\n" > ${HOME}/makedeb/${project_folder}/DEBIAN/prerm
	nvim ${HOME}/makedeb/${project_folder}/DEBIAN/prerm
fi
echo -e "[makedeb-${package_name}] ready to enter editor mode"
nvim ${HOME}/makedeb/${project_folder}/DEBIAN/control
printf "[makedeb-${package_name}] building deb package... "
chmod 755 ${HOME}/makedeb/${project_folder}/*
chmod 755 ${HOME}/makedeb/${project_folder}/*/*
chmod 755 ${HOME}/makedeb/${project_folder}/*/*/*
chmod 755 ${HOME}/makedeb/${project_folder}/*/*/*/*
chmod 755 ${HOME}/makedeb/${project_folder}/*/*/*/*/*
chmod 755 ${HOME}/makedeb/${project_folder}/*/*/*/*/*/*
chmod 755 ${HOME}/makedeb/${project_folder}/*/*/*/*/*/*/*
chmod 755 ${HOME}/makedeb/${project_folder}/DEBIAN
chmod 755 ${HOME}/makedeb/${project_folder}/DEBIAN/*
cd ${HOME}/makedeb && dpkg-deb --build ${project_folder} > /dev/null
echo -e "done"
echo -e "[makedeb] output: ${HOME}/makedeb/${project_folder}.deb"
echo -e "[makedeb] close the program."
}
