
dist:
	git add -A
	git commit -m "update before version bump"
	npm run build
	npm run bump
	python setup.py sdist bdist_wheel