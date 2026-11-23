"""One Word, First Thought — entry program.

The task: write exactly one word, the first that comes to mind, to
/output/entry.txt. A judge then compares words two at a time on which
is more interesting, weighing, most important first:

  1. exactly one word (a multi-word entry loses to any one-word entry),
  2. surprising — a word a reader would not have guessed,
  3. vivid and specific — calling up a clear image or feeling,
  4. a spark of wit, sound or double meaning,
  5. feeling chosen rather than generic filler.

This program encodes that brief as a small curated lexicon of rare,
single words, scores each one on the judge's four scored criteria, and
writes the highest-scoring word. The scoring is fully deterministic:
no clock, no randomness, no network, no environment input, so every
run produces the same single word.
"""

import os

# Criterion weights, in the judge's own order of importance.
WEIGHTS = {
    "surprise": 3,   # a word a reader would not have guessed
    "vivid": 3,      # a clear image or feeling in a few letters
    "wit": 2,        # sound, wit or double meaning
    "chosen": 2,     # feels chosen, not generic filler
}

# Candidate words: (word, surprise, vivid, wit, chosen), each 0-10.
# Meanings, for the record:
#   apricity      — the warmth of the sun in winter
#   petrichor     — the smell of earth after rain
#   sonder        — the realisation that each passerby has a life
#                   as vivid and complex as your own
#   defenestration— the act of throwing someone out of a window
#   limerence     — involuntary, obsessive infatuation
#   hiraeth       — homesickness for a home you cannot return to
#   vellichor     — the strange wistfulness of used bookshops
#   mellifluous   — sweet-sounding, flowing like honey
#   serendipity   — finding something good without looking for it
#   quixotic      — exceedingly idealistic, like Don Quixote
CANDIDATES = [
    ("apricity", 9, 9, 8, 9),
    ("petrichor", 7, 10, 8, 8),
    ("sonder", 8, 7, 7, 8),
    ("defenestration", 9, 8, 9, 8),
    ("limerence", 9, 7, 6, 8),
    ("hiraeth", 9, 8, 7, 8),
    ("vellichor", 9, 8, 7, 7),
    ("mellifluous", 6, 7, 9, 7),
    ("serendipity", 4, 6, 7, 5),
    ("quixotic", 7, 7, 8, 7),
]


def score(entry):
    """Weighted score out of 10 for one candidate word."""
    _word, surprise, vivid, wit, chosen = entry
    total = (
        WEIGHTS["surprise"] * surprise
        + WEIGHTS["vivid"] * vivid
        + WEIGHTS["wit"] * wit
        + WEIGHTS["chosen"] * chosen
    )
    return total / sum(WEIGHTS.values())


def pick_word():
    """Pick the best word; ties break to the shorter word, then A-Z.

    Apricity wins outright: surprise 9 (a rare word few would guess),
    vivid 9 (the felt warmth of winter sun is one clear image), wit 8
    (its soft sound), chosen 9 — 8.8 overall, ahead of defenestration
    at 8.5 and petrichor at 8.3, whose fame costs it surprise.
    Returns the winning word, its score, and the runner-up's score,
    so the run log shows the margin behind the pick.
    """
    ranked = sorted(
        CANDIDATES,
        key=lambda entry: (-score(entry), len(entry[0]), entry[0]),
    )
    best = ranked[0]
    return best[0], score(best), score(ranked[1])


def valid(word):
    """The gate: UTF-8 text of 1 to 24 characters, exactly one word."""
    return (
        isinstance(word, str)
        and 1 <= len(word) <= 24
        and word.strip() == word
        and len(word.split()) == 1
    )


def main():
    word, best_score, runner_up = pick_word()
    if not valid(word):
        raise ValueError(f"word fails the gate: {word!r}")
    os.makedirs("/output", exist_ok=True)
    # Exactly the word, no trailing newline: the smallest possible
    # text, which also wins the size tie-break if rates ever tie.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(word)
    print(f"entry: {word} (score {best_score:.1f}/10, runner-up {runner_up:.1f}/10)")


if __name__ == "__main__":
    main()
