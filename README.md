# Sarvam AI Skill for OpenClaw

Complete Indian language AI suite for OpenClaw - Text-to-Speech, Speech-to-Text, Translation, Transliteration, and Document Intelligence.

[![GitHub](https://img.shields.io/badge/GitHub-ankitjh4%2Fsarvam--ai--skill-blue)](https://github.com/ankitjh4/sarvam-ai-skill)
[![Sarvam AI](https://img.shields.io/badge/Sarvam%20AI-Docs-green)](https://docs.sarvam.ai)

## Features

- **Bulbul v3 TTS** - 30+ speaker voices, 11 Indian languages, 2500 char limit
- **Saarika STT** - Real-time, batch, and streaming transcription
- **Text Translation** - 22 scheduled Indian languages
- **Transliteration** - Script conversion preserving pronunciation
- **Document Intelligence** - PDF text extraction
- **Chat Completions** - Sarvam LLM API

## Installation

### Prerequisites

Install the official Sarvam Python SDK:

```bash
pip install sarvamai
```

### OpenClaw Installation

```bash
# Via vett
vett add ankitjh4/sarvam-ai-skill

# Or manual
mkdir -p ~/.openclaw/skills/sarvam-ai
curl -o ~/.openclaw/skills/sarvam-ai/SKILL.md https://raw.githubusercontent.com/ankitjh4/sarvam-ai-skill/main/SKILL.md
```

## Configuration

Set your API key:

```bash
export SARVAM_API_KEY="your-api-key-here"
```

Get your API key at: [dashboard.sarvam.ai](https://dashboard.sarvam.ai)

## Quick Start

```python
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])

# TTS
client.text_to_speech.convert(
    text="नमस्ते, आप कैसे हैं?",
    target_language_code="hi-IN",
    speaker="meera"
)

# STT
client.speech_to_text.transcribe(
    file=open("audio.wav", "rb"),
    language_code="hi-IN"
)
```

## Documentation

See [SKILL.md](./SKILL.md) for complete API reference.

## License

MIT
