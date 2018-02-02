default: main

main:
	python3 common/lista2tex.py < lista.txt > main.tex
	rubber -d main.tex

part:
	python3 common/lista2tex.py < plista.txt > main.tex
	rubber -d main.tex

egy:
	rubber -d egy.tex

clean:
	rubber --clean main
	rubber --clean egy
	rm -f *.pdf