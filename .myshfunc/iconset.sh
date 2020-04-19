
iconset() {
# Usage: iconset project_name icon.png
if test ! -d $HOME/appicon; then
	mkdir $HOME/appicon
fi
hdpi="/sdcard/AppProjects/$1/app/src/main/res/drawable-hdpi"
mdpi="/sdcard/AppProjects/$1/app/src/main/res/drawable-mdpi"
xhdpi="/sdcard/AppProjects/$1/app/src/main/res/drawable-xhdpi"
xxhdpi="/sdcard/AppProjects/$1/app/src/main/res/drawable-xxhdpi"
rm ${hdpi}/ic_launcher.png
rm ${mdpi}/ic_launcher.png
rm ${xhdpi}/ic_launcher.png
rm ${xxhdpi}/ic_launcher.png
cp $2 $HOME/appicon/ic_launcher.png
cp $HOME/appicon/ic_launcher.png ${hdpi}
cp $HOME/appicon/ic_launcher.png ${mdpi}
cp $HOME/appicon/ic_launcher.png ${xhdpi}
cp $HOME/appicon/ic_launcher.png ${xxhdpi}
}
