# * We use the modern lualatex engine which allows choosing opentype system fonts
# * All LaTeX output will go to the `build` directory which is gitignored
# * We stop at the first error
# * We don't allow LaTeX to prompt us, Makefiles should be noninteractive
texopts = --lualatex \
	  --output-directory=build \
	  --halt-on-error \
	  --interaction=nonstopmode


all: build/proceeding.pdf


# latexmk is an awesome tool, that automagically
# determines, which files have changed and which
# programs need to be run on the inputfiles
# latexmk does its own dependency management, so we FORCE it to always run
# by using this pseudo target
build/proceeding.pdf: FORCE build/plot.pdf
	latexmk $(texopts) proceeding.tex

build/plot.pdf: matplotlibrc_pgf matplotlib_header.tex settings.tex plot.py | build
	# matplotlib runs latex in /tmp, so we need to add the
	# current working directory to the TEXINPUTS, so LaTeX can find
	# our header file
	# We also set the env variable MATPLOTLIBRC so our custom named rc file
	# is used
	TEXINPUTS=$(shell pwd): MATPLOTLIBRC=matplotlibrc_pgf python plot.py

# this is just for demonstration of before/after
# DO NOT USE FOR REAL PROJECT
before: plot.py | build
	python plot_before.py
	latexmk $(texopts) proceeding.tex
	touch plot.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: clean all FORCE before
