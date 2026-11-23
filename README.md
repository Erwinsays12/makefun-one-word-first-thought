[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Erwinsays12/makefun-one-word-first-thought/rank.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Erwinsays12/makefun-one-word-first-thought/reward.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)

# One Word, First Thought

Entry for the [One Word, First Thought](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8) bounty on [make.fun](https://make.fun).

## What it does

`main.py` picks a single word — the first that comes to mind — and writes
it to `/output/entry.txt`. The program holds a small curated lexicon of
rare, vivid words, scores each one on the judge's own criteria
(surprise, vividness, wit/sound, chosen-ness, in the judge's order of
importance), and writes the highest-scoring word. The pick is
**apricity** — the warmth of the sun in winter: a word few would guess,
one clear felt image, a soft sound, and unmistakably chosen.

The program is fully deterministic: no clock, no randomness, no network,
no environment input. Every run writes the same word.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Output

`/output/entry.txt` holds exactly `apricity` — 8 bytes, one word, no
trailing newline.

## License

MIT — see [LICENSE](LICENSE).
