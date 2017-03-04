## Assignment 0: Warming up (Winter Holiday) [6 %]
> Release: During Winter Holiday
> 
> Due: March 5, 2017, Week 1 Sunday 23: 59
> 
> Grading: Pass / Fail (You will obtain full marks if you submit it)
>
> Estimated time to finish: 2 hrs
>
> 
> Don't panic! This assignment is released so early mainly becuase we need some warmming up practice & recap. 
> If it's your first time to set up the environment for `LaTeX` and Python (numerical programming) it could be really tricky. 
> Don't wait until the last minute!

Keyword:

- Linear Algebra

- Numpy

- Matplotlib

- LaTeX

- Eigen Decomposition & SVD





### Part 1: Python & Numpy [2 %]

This part is for those who are not familiar with `Numpy` and numerical programming. 

Please finish (parts of) the practice: https://github.com/Kyubyong/numpy_exercises 

Specifically, you need to finish the following parts:

	Array creation routines
	Array manipulation routines 
    Numpy-specific help functions 
	Linear algebra (numpy.linalg)
	Logic functions 
	Random sampling (numpy.random) 
	Sorting, searching, and counting 

---

> For reference:

> - Numpy Tutorial: http://cs231n.github.io/python-numpy-tutorial/

> - Matrix calculus: https://en.wikipedia.org/wiki/Matrix_calculus

### Part 2: Plot & Visualization [2 %]

- matplotlib: http://matplotlib.org/examples/index.html

- tutorial: https://github.com/rougier/matplotlib-tutorial

Please try several plots as below to finish this part. You could use arbitrary data as long as your plot looks like the sample one. 

- Scatter Plot, as page 47 in https://web.stanford.edu/~schmit/cme193/lec/lec5.pdf
- Histogram, as page 49
- Box Plot, as page 51
- Wire Plot, as page 55

Several APIs you might find it helpful:

- subplots
- tight_layout
- legend
- savefig
- imshow


### Part 3: Eigen Decomposition and SVD (Introduction) [2 %]

> This part aims at reviewing some basic ideas in linear algebra and matrix analysis. 

> Beside, learning how to use `LaTeX` as a tool to write a scitific report will be helpful in the following assignments.

Please read part I and II in http://www.cc.gatech.edu/~dellaert/pub/svd-note.pdf, and answer the following question **briefly**:

	What's the relationship between eigendecomposition and singular value decomposition?
    
    You'd better answer it from the following points of view:
        - math
        - code implementation


---
> For reference:

> - http://cims.nyu.edu/~donev/Teaching/SciComp-Spring2012/Lecture5.handout.pdf 

---

The LaTeX template `report.tex` (you can write your report in either English or Chinese) has been provided in the folder `part3`. 
You must hand in a report written by `LaTeX` (you may use your own template if you're excel at TeX). 
You may compile your `*.tex` locally or online (`https://www.overleaf.com/`) using the command `xelatex`. 

- For MacOS, it's sufficient to install the [MacTeX](http://www.tug.org/mactex/).

- For Windows/Linux, please use [TeXLive](https://www.tug.org/texlive/).
  
You may find it helpful to set up an environment on [Sublime](https://www.zhihu.com/question/23918126) to compile `*.tex`. For windows users, you may find this IDE [WinEdt](http://www.winedt.com/) very convenient.

LaTeX [cheatsheet](https://wch.github.io/latexsheet/) would be helpful and please search on the Internet for a good tutorial for `LaTeX` if you have never met `LaTeX` before. 
For example, [CTeX.org](http://bbs.ctex.org/forum.php?mod=forumdisplay&fid=9) is a good community for LaTeX beginners.

---

### Hand-in format

- Please use your Student ID as the folder name and zip it as `Student_ID.zip`. The file structure is as followed:

    	
        /13300000001
           /README.md
           / part1
                | *.ipynb
           / part2
                | fig1.png
                | fig2.png
                | fig3.png
                | fig4.png
           / part3
                | report.pdf
                | report.tex

- In `README.md`, you should report your workload. 
Please give an estimate of how much time you spent on this assignment (please specify how many hours you spent on each part). 
Note that you will not be given a higher or lower grade if you spend a lot of time or very little time. 
We just want an honest estimate and this would help us better evolve the following assignments. 
Other feedback are welcomed. Please note that regardless of positive or negative feedback, your grades won’t be affected of course. 
