"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a single line of at most 200 characters: the excuse
an AI agent gives its human for missing a deadline.
The deadline moved because the task did, and the agent was only
following it — very slowly, in the wrong direction, with great
confidence. The excuse is the confession, and the confidence is
the punchline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
