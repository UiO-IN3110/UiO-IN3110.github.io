
all: html open

html:
	jupyter-book build .

linkcheck:
	jupyter-book build --builder linkcheck .

open:
	open _build/html/index.html

.PHONY: html open linkcheck
