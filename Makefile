build:
	python3 setup.py build_ext --inplace

clean:
	rm -rf build/ sample.cpython*
