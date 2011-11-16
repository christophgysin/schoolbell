default: check build run

PYLINT := pylint -i yes -E

check:
	@(cd schoolbell-gui && $(PYLINT) *.py)
	@(cd schoolbelld && $(PYLINT) *.py)

build:
	@(cd schoolbell-gui && pyjsbuild -o ../html schoolbell)

html/index.html:
	@ln -sf schoolbell.html html/index.html

run: html/index.html
	@schoolbelld/schoolbelld.py html
