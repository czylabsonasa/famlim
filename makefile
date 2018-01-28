default: main

main:
	python3 lista2osszes.py < lista.txt > main.tex
	rubber -d main.tex
clean:
	rubber --clean main
	rm *.pdf