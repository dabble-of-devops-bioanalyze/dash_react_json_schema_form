
dist:
	git add -A
	git commit -m "update before version bump"
	git push origin main
	rm -rf dist
	npm run build
	npm run bump
	python setup.py sdist bdist_wheel
	twine upload dist/*.whl

tsx:
	# I wanted to use some source files from @rjsf/bootstrap
	npx tsc --jsx preserve -t es2020 --outDir js --noEmit false

build:
	npm run build

watch:
	python ./watch.py

dev/up:
	npm run build
	python usage.py