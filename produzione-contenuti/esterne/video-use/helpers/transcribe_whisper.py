"""Trascrizione gratuita in locale con faster-whisper (alternativa a ElevenLabs Scribe).

Aggiunta da Ricciardi Food Agency: scrive in <edit_dir>/transcripts/<video>.json lo stesso
formato di transcribe.py (lista "words" con type word/spacing, start, end, speaker_id),
così pack_transcripts.py e render.py funzionano senza chiave API.
Limiti rispetto a Scribe: niente separazione dei parlanti (tutto S0) e niente eventi audio
tipo (laughs); i timestamp delle parole sono un po' meno precisi, quindi tenere il padding
dei tagli verso l'alto (100-200 ms).

Uso:
    pip install faster-whisper
    python helpers/transcribe_whisper.py <video> [--edit-dir DIR] [--language it]
                                         [--model small|medium] [--prompt "fassona, burrata"]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path


def extract_audio(video: Path, dest: Path) -> None:
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(video), "-map", "0:a:0", "-vn", "-ac", "1",
         "-ar", "16000", "-c:a", "pcm_s16le", str(dest)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--edit-dir", default=None)
    ap.add_argument("--language", default="it")
    ap.add_argument("--model", default="small")
    ap.add_argument("--prompt", default=None, help="vocabolario: nomi di piatti, prodotti, locale")
    args = ap.parse_args()

    video = Path(args.video).resolve()
    edit_dir = Path(args.edit_dir) if args.edit_dir else video.parent / "edit"
    out = edit_dir / "transcripts" / f"{video.stem}.json"
    if out.exists():
        print(f"cached: {out}")
        return
    out.parent.mkdir(parents=True, exist_ok=True)

    from faster_whisper import WhisperModel

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "audio.wav"
        extract_audio(video, wav)
        # audio passato come array: evita la decodifica con PyAV (incompatibile in alcune versioni)
        import wave
        import numpy as np
        with wave.open(str(wav), "rb") as wf:
            pcm = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16)
        audio = pcm.astype(np.float32) / 32768.0
        segments, info = model.transcribe(
            audio, language=args.language, word_timestamps=True,
            initial_prompt=args.prompt, vad_filter=False,
        )
        words: list[dict] = []
        prev_end = None
        for seg in segments:
            for w in seg.words or []:
                start, end = round(w.start, 3), round(w.end, 3)
                if prev_end is not None and start > prev_end:
                    words.append({"type": "spacing", "text": " ", "start": prev_end,
                                  "end": start, "speaker_id": "speaker_0"})
                words.append({"type": "word", "text": w.word.strip(), "start": start,
                              "end": end, "speaker_id": "speaker_0"})
                prev_end = end

    data = {
        "language_code": info.language,
        "text": " ".join(w["text"] for w in words if w["type"] == "word"),
        "words": words,
        "source": "faster-whisper",
    }
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    print(f"ok: {out} ({sum(1 for w in words if w['type'] == 'word')} parole)")


if __name__ == "__main__":
    main()
