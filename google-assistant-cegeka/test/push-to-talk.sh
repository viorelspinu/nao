
ffmpeg -i ./sound_record.ogg audio.wav -y
ffmpeg -i ./audio.wav -ar 11025 -ac 2 output.wav -y

googlesamples-assistant-pushtotalk --project-id nao4-c96b5 --device-model-id nao4-c96b5-nao123-fas3dg --input-audio-file ./output.wav --output-audio-file ./response.wav

afplay ./response.wav