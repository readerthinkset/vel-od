"""
MMS Odia TTS Engine (Meta Massively Multilingual Speech)
100% Free, Local, Offline, No API key, No company registration required.
Uses Meta's facebook/mms-tts-ory VITS model.
"""

import os
import subprocess
from pathlib import Path

_model = None
_tokenizer = None


def get_mms_odia_model():
    global _model, _tokenizer
    if _model is None:
        import torch
        from transformers import VitsModel, AutoTokenizer
        model_id = "facebook/mms-tts-ory"
        print("[mms-odia] Loading local Meta MMS Odia model...")
        _tokenizer = AutoTokenizer.from_pretrained(model_id)
        _model = VitsModel.from_pretrained(model_id)
        _model.eval()
    return _model, _tokenizer


def generate_odia_audio(text: str, output_path: str) -> bool:
    """
    Synthesize native Odia speech and save to output_path (supports .mp3 or .wav).
    """
    try:
        import torch
        import scipy.io.wavfile

        model, tokenizer = get_mms_odia_model()

        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            output = model(**inputs).waveform

        audio_arr = output.squeeze().cpu().numpy()
        rate = model.config.sampling_rate

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        temp_wav = out.with_suffix(".temp.wav")

        scipy.io.wavfile.write(str(temp_wav), rate=rate, data=audio_arr)

        if out.suffix.lower() == ".mp3":
            cmd = [
                "ffmpeg", "-y",
                "-i", str(temp_wav),
                "-acodec", "libmp3lame",
                "-b:a", "192k",
                str(out)
            ]
            res = subprocess.run(cmd, capture_output=True)
            if temp_wav.exists():
                try:
                    temp_wav.unlink()
                except Exception:
                    pass
            if res.returncode != 0:
                print(f"[mms-odia] ffmpeg MP3 conversion failed: {res.stderr.decode('utf-8', errors='ignore')}")
                return False
        else:
            if temp_wav != out:
                if out.exists():
                    out.unlink()
                temp_wav.rename(out)

        if out.exists() and out.stat().st_size > 500:
            print(f"[mms-odia] Generated Odia audio -> {out.name} ({out.stat().st_size} bytes)")
            return True
        return False

    except Exception as e:
        print(f"[mms-odia] Error generating Odia audio: {e}")
        return False
