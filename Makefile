default: check build run

check:
	@pylint -E schoolbell-gui/schoolbell.py

build:
	@(cd schoolbell-gui && pyjsbuild -o ../html schoolbell)

html/index.html:
	@ln -sf schoolbell.html html/index.html

run: html/index.html
	@schoolbelld/schoolbelld.py html
