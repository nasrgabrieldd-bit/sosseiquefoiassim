#!/usr/bin/env bash
# Prepara uma sessão nova: dependências Python e modelo de voz Kokoro (baixado do GitHub, não versionado).
set -euo pipefail
MODELOS="${MODELOS:-$HOME/tts}"
pip install -q --break-system-packages kokoro-onnx soundfile pillow numpy fonttools 2>/dev/null || pip install -q kokoro-onnx soundfile pillow numpy fonttools
mkdir -p "$MODELOS"
base="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"
[ -s "$MODELOS/kokoro-v1.0.onnx" ] || curl -sL -o "$MODELOS/kokoro-v1.0.onnx" "$base/kokoro-v1.0.onnx"
[ -s "$MODELOS/voices-v1.0.bin" ]  || curl -sL -o "$MODELOS/voices-v1.0.bin"  "$base/voices-v1.0.bin"
command -v ffmpeg >/dev/null || { echo "ffmpeg ausente"; exit 1; }
echo "ok: modelos em $MODELOS"
