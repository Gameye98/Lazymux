
fbvid(){
# Usage: fbvid "POST_URL"
if test -d ~/fbvid; then
        true
else
        mkdir ~/fbvid
fi
if test -d ~/fbvid/output; then
        true
else
        mkdir ~/fbvid/output
fi
cd ~/fbvid
url="$1"
youtube-dl -F ${url}
read -p "audio format: " fbaudio
read -p "video format: " fbvideo
audioext="m4a"
videoext="mp4"
echo -e "[fbvid] url: ${url}"
echo -e "[fbvid] downloading the audio..."
youtube-dl -f ${fbaudio} ${url}
echo -e "[fbvid] downloading the video..."
youtube-dl -f ${fbvideo} ${url}
ex=(${url//\// })
audiofile="$(ls | grep ${audioext})"
videofile="$(ls | grep ${videoext})"
echo -e "[fbvid] add the audio to the video..."
ffmpeg -i "${videofile}" -i "${audiofile}" -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k "${ex[4]}.${videoext}"
rm "${audiofile}"
rm "${videofile}"
mv "${ex[4]}.${videoext}" output
echo -e "[fbvid] done. output: output/${ex[4]}.${videoext}"
}
