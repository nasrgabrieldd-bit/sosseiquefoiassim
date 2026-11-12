#!/usr/bin/env bash
# produz.sh EP_DIR [etapa]: narra -> eventos/audio -> video -> mix
set -e
EP=$1; P=$(cd "$(dirname "$0")" && pwd)
[ -f $EP/voz.wav ] || python3 $P/narra.py $EP/roteiro.json $EP >/dev/null
D=$(python3 $P/motor.py $EP eventos)
python3 $P/audio_extra.py $EP/eventos.json $D $EP >/dev/null
python3 $P/motor.py $EP video >/dev/null
python3 $P/motor.py $EP capa >/dev/null
ID=$(basename $EP)
ffmpeg -loglevel error -y -i $EP/video_mudo.mp4 -i $EP/voz.wav -i $EP/trilha.wav -i $EP/efeitos.wav -filter_complex "[1:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[v][vsc];[2:a]volume=0.10[m];[m][vsc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=400[md];[3:a]volume=0.75[fx];[v][md][fx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart $EP/$ID.mp4
echo "$ID ok $(ffprobe -v error -show_entries format=duration -of csv=p=0 $EP/$ID.mp4)"
