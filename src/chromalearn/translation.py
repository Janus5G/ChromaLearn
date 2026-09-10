import argparse
import json
from pathlib import Path

import storage
from model import call_model

ALLOWED_SUFFIXES = {'.md', '.txt', '.json'}
MAX_BYTES = 200_000
DRAFT_BANNER = 'MASKINOVERSAT KLADDE - KRÆVER MENNESKELIG GODKENDELSE'


def _check_input(path: Path):
    path = path.expanduser().resolve()
    if not path.is_file():
        raise ValueError('Inputfilen findes ikke')
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        raise ValueError('Kun .md, .txt og .json understøttes')
    if path.stat().st_size > MAX_BYTES:
        raise ValueError('Filen er for stor til oversættelsesværktøjet (maks. 200 kB)')
    text = str(path)
    forbidden = ('/var/lib/chromalearn/profiles/', '/etc/chromalearn/config.json')
    if any(x in text for x in forbidden):
        raise ValueError('Denne ChromaLearn-driftsfil må ikke sendes til oversættelsesfunktionen')
    return path


def _translate_markdown(config, text: str, language: str):
    system = (
        'You are a careful translation engine for open-source educational software documentation. '
        'Translate the supplied static document to the requested language. Preserve Markdown structure, '
        'code blocks, commands, filenames, URLs, identifiers, version numbers and legal references exactly. '
        'Do not add claims, legal conclusions or explanations. Return only the translated document.'
    )
    prompt = f'Target language: {language}\n\nDOCUMENT:\n{text}'
    return call_model(config, [{'role': 'system', 'content': system}, {'role': 'user', 'content': prompt}]).strip()


def _translate_json(config, text: str, language: str):
    obj = json.loads(text)
    system = (
        'Translate JSON string VALUES to the requested language. Preserve every key, JSON structure, '
        'identifier, URL, path, code token, placeholder and number. Return valid JSON only. '
        'Do not add or remove keys and do not add commentary.'
    )
    prompt = f'Target language: {language}\n\nJSON:\n{json.dumps(obj, ensure_ascii=False, indent=2)}'
    raw = call_model(config, [{'role': 'system', 'content': system}, {'role': 'user', 'content': prompt}])
    start, end = raw.find('{'), raw.rfind('}')
    if start < 0 or end < start:
        raise ValueError('AI-serveren returnerede ikke gyldig JSON')
    translated = json.loads(raw[start:end+1])
    if _key_shape(translated) != _key_shape(obj):
        raise ValueError('Oversættelsen ændrede JSON-strukturen og blev afvist')
    return json.dumps(translated, ensure_ascii=False, indent=2, sort_keys=False) + '\n'


def _key_shape(value):
    if isinstance(value, dict):
        return ('dict', tuple((k, _key_shape(v)) for k, v in value.items()))
    if isinstance(value, list):
        return ('list', tuple(_key_shape(v) for v in value))
    return type(value).__name__


def translate_file(input_path, language, code, output=None, config=None):
    src = _check_input(Path(input_path))
    text = src.read_text(encoding='utf-8')
    config = config or storage.load_config()
    if src.suffix.lower() == '.json':
        translated = _translate_json(config, text, language)
        # JSON cannot carry a comment banner; companion review file is created below.
    else:
        translated = f'> **{DRAFT_BANNER}**  \n> Mål­sprog: {language}. Gennemgå teksten menneskeligt før officiel brug.\n\n' + _translate_markdown(config, text, language) + '\n'

    if output:
        dest = Path(output).expanduser()
    else:
        dest = Path.cwd() / 'translations' / code / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(translated, encoding='utf-8')
    review = dest.with_suffix(dest.suffix + '.REVIEW.txt')
    review.write_text(
        f'{DRAFT_BANNER}\nKilde: {src}\nMålsprog: {language} ({code})\n'
        'AI-assisteret oversættelse. Skal menneskegennemgås før officiel brug.\n'
        'Må ikke anvendes som bevis for juridisk korrekt oversættelse.\n',
        encoding='utf-8'
    )
    return dest, review


def main(argv=None):
    parser = argparse.ArgumentParser(description='Lav en AI-assisteret oversættelseskladde af statiske ChromaLearn-filer.')
    parser.add_argument('input', help='Kilde-fil (.md, .txt eller .json)')
    parser.add_argument('--language', required=True, help='Målsprog, fx English eller Deutsch')
    parser.add_argument('--code', required=True, help='Kort sprogkode, fx en eller de')
    parser.add_argument('--output', help='Valgfri outputsti')
    args = parser.parse_args(argv)
    dest, review = translate_file(args.input, args.language, args.code, args.output)
    print(f'Oversættelseskladde: {dest}')
    print(f'Krav om menneskelig review: {review}')


if __name__ == '__main__':
    main()
