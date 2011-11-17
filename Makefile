default: check build run

PYLINT := pylint -i yes -E

check:
	@(cd schoolbell-gui && $(PYLINT) *.py)
	@(cd schoolbelld && $(PYLINT) *.py)

build:
	@(cd schoolbell-gui && pyjsbuild -o ../html schoolbell)

html/index.html:
	@ln -sf schoolbell.html html/index.html

html/alarms.json.conf:
	@cp alarms.json.conf html

run: html/index.html html/alarms.json.conf
	@schoolbelld/schoolbelld.py html
