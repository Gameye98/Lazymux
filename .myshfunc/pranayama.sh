
pranayama() {
# Usage: pranayama
#           or
#        pranayama [n]
if test -z "$1"; then
	repeat=4
else
	repeat="$1"
fi
for((x = 0;x < ${repeat};x++)); do
	termux-tts-speak "Inhale"
	sleep 4
	termux-tts-speak "Hold your breath"
	sleep 7
	termux-tts-speak "Exhale"
	sleep 8
done
}
