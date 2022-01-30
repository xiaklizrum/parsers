# Parsers bundle
## Current list
* [AMOcrm-partners](parsers/amocrm-partners)
* [jsontoxlsx](parsers/jsontoxlsx)
* [zadarma](parsers/zadarma-lite)
## Run docker container
```
docker run -v $(pwd):/tmp `container-tag` python `path-to-python-file`
```
for zadarma lite parser
```
docker run -v $(pwd):/tmp xiaklizrum/parsers python parsers/zadarma-lite/main.py
```