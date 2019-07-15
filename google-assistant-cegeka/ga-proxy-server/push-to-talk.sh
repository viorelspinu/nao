export LC_ALL=C.UTF-8
export LANG=C.UTF-8

ffmpeg -i ./sound_record.wav audio.wav -y
ffmpeg -i ./audio.wav -ar 11025 -ac 2 output.wav -y

googlesamples-assistant-pushtotalk --project-id $PROJECT_ID --device-model-id $DEVICE_ID --input-audio-file ./output.wav --output-audio-file ./response.wav

ffmpeg -i ./response.wav -ac 2 -filter:a "volume=7" response_robot.wav -y

#afplay ./response_robot.wav