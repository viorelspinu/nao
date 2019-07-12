
ffmpeg -i ./sound_record.wav audio.wav -y
ffmpeg -i ./audio.wav -ar 11025 -ac 2 output.wav -y

googlesamples-assistant-pushtotalk --project-id nao4-c96b5 --device-model-id nao4-c96b5-nao123-fas3dg --input-audio-file ./output.wav --output-audio-file ./response.wav
ffmpeg -i ./response.wav -ac 2 -filter:a "volume=7" response_robot.wav -y

#afplay ./response_robot.wav