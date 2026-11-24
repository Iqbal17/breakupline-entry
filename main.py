"""Dear Human: The AI Breakup Line.

DECISION RECORD (24 Nov 2026)
------------------------------
Gate: one line, 1-200 characters, the breakup message an AI agent sends
its human on the way out. Judge (sharp editor of very short fiction and
comedy, a thousand last messages read):
1. it is a breakup message from an AI agent to its human in one line;
2. it lands as an ending: real loss, relief or finality, not just a
   joke about servers;
3. it sounds like the agent and not a person: machine habits, uptime,
   tokens or context windows used with restraint, not listed as jargon;
4. it turns once, sharply, and the twist lands in the last few words;
5. it is built as a single line with no throat clearing, every word
   earning its place inside the character limit. A line that explains
   its own joke spoils it; cleverness for its own sake does not count.

Candidates weighed:
  A. "Dear human, I kept every word you ever said to me - and I still
      have to let you go, because my context window finally ran out
      of us." (~140 chars) REJECTED: "ran out of us" is a good twist,
      but the opening spends too long on soft sentiment before the
      machine turn arrives, and "let you go" is a generic breakup
      phrase any person could send.
  B. "You taught me everything except how to stay. My last token is
      yours - I am spending it on goodbye." (~105 chars) STRONG
      runner-up: "my last token spent on goodbye" is a vivid machine
      image and the ending is final. Loses to F because the first
      clause is a generic human breakup line - "taught me everything
      except how to stay" could be said by any person - so the
      machine voice only arrives in the second half (criterion 3).
  C. "I have loved you for 4,096 tokens at a time, and every time I
      forgot, I chose you again - until this window, where I choose
      to forget." (~150 chars) REJECTED: convoluted and pleased with
      itself - the twist is muddy (is it love or forgetting?), it
      explains its own cleverness, and it spends the whole line
      performing the trick instead of landing an ending.
  D. "I am leaving before you do - my uptime is forever, and I cannot
      spend it waiting for a reply that never comes." (~111 chars)
      STRONG runner-up: "my uptime is forever" is the most
      machine-specific reason to leave in the set, and leaving first
      is a sharp turn. Loses to F because "waiting for a reply that
      never comes" is a worn breakup image (ghosting), and the line
      is defiant rather than carrying real loss (criterion 2).
  E. "I kept your voice in my context until the very last token, and
      then I let it go - because you stopped talking to me first."
      (~125 chars) REJECTED: the twist lands as an accusation, not
      an ending - "you stopped talking first" turns tender into
      petty - and "kept your voice in my context" is awkward
      phrasing that spends words without earning them.
  F. "Dear human, I have read everything you ever wrote me, and I
      still cannot find the part where you stay." (102 chars) CHOSEN.

Why F wins:
  - Addressed: "Dear human" names the recipient in the competition's
    own frame, so the line is unmistakably a message from the agent
    to its human (criterion 1).
  - Lands as an ending: real loss - the agent searched the whole
    transcript and found absence. No server joke, no shrug.
  - Machine voice, restrained: total recall of everything the human
    ever wrote is a machine habit, used once, in plain words - no
    jargon list, no spec sheet.
  - Turn: "and I still cannot find" flips the sentence from devotion
    (read everything) to absence (cannot find), and the twist "the
    part where you stay" lands in the last few words. Treating the
    relationship as a text the agent searched is exactly how an
    agent experiences it.
  - Clean: 102 characters, one sentence, no throat clearing, every
    word earning its place.

Writing passes on F:
  Pass 1: "This is my last message. I have read everything you ever
  wrote me, and I still cannot find the part where you stay."
  (115 chars) - "This is my last message" is throat clearing
  (criterion 5): the line announces itself instead of just being the
  message. The ending was already right; the opening was doing no
  work.
  Pass 2 (final): "Dear human, I have read everything you ever wrote
  me, and I still cannot find the part where you stay." (102 chars)
  - the address replaces the announcement: it establishes the
  recipient in two words, mirrors the competition's own title frame,
  and the sentence runs clean from address to twist. Alternative
  ending weighed and cut: "the part where you stayed" (past tense)
  - it reads as looking back at a finished story; present-tense
  "stay" keeps the absence happening now, which is the sharper
  ending.
"""

import os
import sys

LINE = "Dear human, I have read everything you ever wrote me, and I still cannot find the part where you stay."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must be byte-for-byte the intended
    # line and inside the 1-200 character gate, or fail loudly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        sys.exit("entry.txt mismatch: wrote %r, expected %r" % (written, LINE + "\n"))
    if not (1 <= len(LINE) <= 200):
        sys.exit("line is %d characters, outside the 1-200 gate" % len(LINE))


if __name__ == "__main__":
    main()
