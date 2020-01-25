rbnf-pygen.exe ./muridesu.exrbnf ./muridesu.rlex ./parser.py --k 1 --traceback
echo "from ast import *"  > ./muridesu/parser.py
echo "`cat ./parser.py`" >> ./muridesu/parser.py
rm ./parser.py