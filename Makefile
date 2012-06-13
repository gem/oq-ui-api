ALL: deploy

deploy:
	./bin/makefile.sh $@

fix:
	./bin/collectstatic_fix.sh

.PHONY: ALL deploy fix