
dist:
	git add -A
	git commit -m "update before version bump"
	rm -rf dist
	npm run build
	npm run bump
	python setup.py sdist bdist_wheel
	twine upload dist/*.whl