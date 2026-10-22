# Build the research note

The checked-in [PDF](logspace_note.pdf) is the six-page English research draft. Its complete [LaTeX source](logspace_note.tex) uses standard LaTeX packages and an inline bibliography.

With a LaTeX installation providing `pdflatex`, run from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error logspace_note.tex
pdflatex -interaction=nonstopmode -halt-on-error logspace_note.tex
```

The second pass resolves cross-references. Rebuilding may change PDF metadata and bytes; mathematical content and successful compilation are the reproducibility targets for this document. Exact-value computations are reproduced separately with `python -B reproduce.py` from the repository root.
