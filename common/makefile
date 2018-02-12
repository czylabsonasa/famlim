default: main

main:
	python3 common/lista2tex.py < lista.txt > main.tex
	rubber -d main.tex

part:
	python3 common/lista2tex.py < plista.txt > main.tex
	rubber -d main.tex

draft:
	python3 common/dbglista2tex.py < lista.txt > draft.tex
	rubber -d draft.tex


clean:
	rubber --clean main
	rm -f *.pdf
	./cleanIt