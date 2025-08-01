# aeolus

This project is a script that takes a term, matches it with a url defined in the json database in the resources folder and takes you to that url so you don't have to remember hundreds of urls.

## To go to a url

```bash
python aeolus.py -m github -g
python aeolus.py --matcher github --go-to
```

## To print the matched url

```bash
python aeolus.py -m github -p
python aeolus.py --matcher github --print-details
```

## To add a url+term to match

```bash
python aeolus.py -t github -u www.github.com
python aeolus.py --add-term github --add-url www.github.com
```