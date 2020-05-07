import sys
import os

if len(sys.argv) != 2:
    print("please enter argv")
    exit(0)

name = sys.argv[1]

if os.path.exists('statements/latex/{}.tex'.format(name)):
    os.system('xelatex -interaction nonstopmode statements/latex/{}.tex'.format(name))

if os.path.exists('{}.aux'.format(name)):
    os.remove('{}.aux'.format(name))
if os.path.exists('{}.fls'.format(name)):
    os.remove('{}.fls'.format(name))
if os.path.exists('{}.log'.format(name)):
    os.remove('{}.log'.format(name))
if os.path.exists('{}.out'.format(name)):
    os.remove('{}.out'.format(name))
if os.path.exists('{}.fdb_latexmk'.format(name)):
    os.remove('{}.fdb_latexmk'.format(name))

if os.path.exists('{}.pdf'.format(name)):
    os.replace('{}.pdf'.format(name), './statements/pdf/{}.pdf'.format(name))
else:
    print("Failed to generate pdf")