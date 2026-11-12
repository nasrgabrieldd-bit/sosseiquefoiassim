#!/usr/bin/env bash
set -e
P=$(cd "$(dirname "$0")" && pwd); EP=$P/../episodios/SSA-001
D=$(python3 $P/render_piloto.py $EP eventos)
python3 $P/audio_extra.py $EP/eventos.json $D $EP >/dev/null
python3 $P/render_piloto.py $EP video >/dev/null
python3 $P/render_piloto.py $EP capa >/dev/null
ffmpeg -loglevel error -y -i $EP/video_mudo.mp4 -i $EP/voz.wav -i $EP/trilha.wav -i $EP/efeitos.wav -filter_complex "[1:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[v][vsc];[2:a]volume=0.10[m];[m][vsc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=400[md];[3:a]volume=0.75[fx];[v][md][fx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart $EP/SSA-001.mp4
rm -f $EP/NR-P001.mp4; echo "SSA-001 ok $(ffprobe -v error -show_entries format=duration -of csv=p=0 $EP/SSA-001.mp4)"
