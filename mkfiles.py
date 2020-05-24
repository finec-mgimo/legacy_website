"""Utility to create files from "mkdocs.yml"""
import yaml
from pathlib import Path

with open("mkdocs.yml",  'r', encoding='utf8') as stream:
    try:
        cfg = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        
def values(x):        
  for section in cfg['nav']:
    xs = [x for x in section.values()]
    elem = xs[0]
    if isinstance(elem, str):
        yield(elem)
    else:
        for z in elem:
           yield [x for x in z.values()][0]
    
files = list(values(cfg['nav']))

# will not create  direcotries
for file in files:
    p = Path(cfg['docs_dir']) / file 
    if not p.exists():
        print(p.resolve())
        p.touch()