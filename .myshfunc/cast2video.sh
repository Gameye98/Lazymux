
cast2video() {
# Usage: cast2video file.cast
echo -e "input: $1"
ttygif --input $1 --output cast2video.gif --fps=33
ffmpeg -f gif -i cast2video.gif -pix_fmt yuv420p -c:v libx264 -movflags +faststart -filter:v crop='floor(in_w/2)*2:floor(in_h/2)*2' cast2video.mp4
echo -e "output: cast2video.mp4"
}
