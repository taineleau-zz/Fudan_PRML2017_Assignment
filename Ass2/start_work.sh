mkdir ../../prml_ass1_partIII
cp *.py *.sh *.tex *.bib ../../prml_ass2_$1
cd ../../prml_ass2_$1
git init
git add .
git commit -m "initial init for ass 2"
