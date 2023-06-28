# TXT-to-CSV-for-dLibra

## How it works

### Formats multiple entries such as theese:

```
1.
Tytuł: [...]
Temat i słowa kluczowe: [...], [...]
Data wydania/powstania dokumentu: [...]
Typ zasobu: [...]
Język: [...]
Archiwum: [...]
Numer zespołu: [...]
Sygnatura: [...]
Paginacja: [...]
```


### Into single CSV files to be inported into dLibra formated like this: 
<sub>(some parameters are hardcoded but can be easily changed in [python file](lista.py))</sub>
```
"uwagi";"[...]"
"Title";"[...]"
"Subject";"[...]"
"Subject";"[...]"
"Publisher";"[...]"
"Date";"[...]"
"nazwazes";"[...]"
"Archiwum";"[...]"
"Rights";"[...]"
"Type";"[...]"
"Format";"[...]"
"sygnatura";"[...]"
"Language";"[...]"
"paginacja";"[...]"
"GroupTitle";"[...]"
```

## How to use

1. place [lista.py](lista.py) in the same folder as the .txt file named ```lista.txt```
2. run the program (e.g. using Jetbrains Pycharm)
3. a number of CSV files will be generated, each named with their according number (e.g. ```123.txt```)
4. the program will also generate a ```lista_updated.txt``` which is a copy of ```lista.txt``` but with fixed numbering issues
