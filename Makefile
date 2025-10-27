convention:
	flake8 src
	isort src

sort:
	isort src

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf build/ dist/ *.egg-info