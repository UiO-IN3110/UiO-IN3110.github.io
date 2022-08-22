out/%-beamer.pdf: %.do.txt
	echo "Compiling $< to $@."
	echo $<
	../misc/make.sh $<

all: $(addprefix out/, $(addsuffix -beamer.pdf, $(basename $(basename $(wildcard *.do.txt)))))
