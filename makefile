default: main

main:
	python3 lista2tex.py < lista.txt > main.tex
	rubber -d main.tex
clean:
	rubber --clean main
	rm -f *.pdf