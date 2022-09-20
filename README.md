# CSC-510-HW2-Fall22-G41
Homework Repo for Software Engineering 22 Group 41

[![Build Status](https://app.travis-ci.com/vishnuchalla/CSC-510-HW2-Fall22-G41.svg?branch=main)](https://app.travis-ci.com/vishnuchalla/CSC-510-HW2-Fall22-G41)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7053897.svg)](https://doi.org/10.5281/zenodo.7053897)

![alt text](https://github.com/vishnuchalla/CSC-510-HW1-Fall22-G41/blob/main/data/softwareEngg.png?raw=true)

Our project is the conversion of this source code: https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf in lua to python.

## Theory
The  function _Y=F(X)_ computes dependent variables _Y_ from independent variables _X_. 
Some variables are `Num`eric (which we denote with a leading upper case letter) and some
are `Sym`bolic. Some `dependent` variables need to minimized (denoted with a trailing `-` sign)
and other need to be maximized (denoted with a trailing `+`).

We say a CSV file contains lots of `X,Y` examples. Line one of the file has a name showing the column
name and types. E.g. in our 
[test file](https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv),
the dependent variables are columns 4,5 and 8. 

```
Clndrs,Volume,Hp:,Lbs-,Acc+,Model,origin,Mpg+
8,304.0,193,4732,18.5,70,1,10
8,360,215,4615,14,70,1,10
8,307,200,4376,15,70,1,10
8,318,210,4382,13.5,70,1,10
8,429,208,4633,11,72,1,10
```

Note also the ":" header on `Hp:` (above). This denotes a column to skip.

You have to report middle and diversity of each non-skipped column.

For numbers:
- mid = median = sort numbers seen so far, return the middle value
- div = standard deviation = sort numbers, find 90th, 10th percentile, return (90th-10th)/2.56
  - why? well you know that 1 or 2 standard deviations captures 66 to 95\% of the mass. So somewhere in-between
    1 and 2 is some point where you catch 90\% (that point is 1.28 standard deviations, so we used
    plus or minus 1.28=2.56)

For symbols:
- mid = mode = most common symbol
- div = entropy = for symbols occurring at probability p1,p2,... then   
     entropy= <em>&sum; -p<sub>i</sub> \* log2(p<sub>i</sub>)</em>.
  - Why? well, entropy can be viewed as  the effort required to recreate a signal. 
  - If a signal has parts
    that occur a probability p1,p2,... 
  - then the probability that we want to search for a signal is, wait for it,
    p1 + p2,.... 
  - And the effort to find the signal is _log2(p)_ (assuming a binary chop)
  - So the probability of needed that search effort is  <em>-p<sub>i</sub> \* log2(p<sub>i</sub>)</em>
    (and the minus sign is added as convention).

## Functionality

The code supports the following five classes : `Data`, `Cols`, `Sym`, `Num`, `Row`. Each class performs a statistical function on the test data based on the constraints.

The code return the following output for the testcases.


```

-----------------------------------
!!!!!!	CRASH	BAD	false

-----------------------------------
!!!!!!	FAIL	LIST	true

-----------------------------------

Examples lua csv -e ...
	ALL
	BAD
	LIST
	LS
	bignum
	csv
	data
	num
	stats
	sym
	the
!!!!!!	PASS	LS	true

-----------------------------------
{1 28 49 50 56 85 86 156 208 237 294 327 444 459 461 485 490 503 
 546 618 653 712 723 727 770 801 849 915 928 941 967 987}
!!!!!!	PASS	bignum	true

-----------------------------------
{Clndrs Volume Hp: Lbs- Acc+ Model origin Mpg+}
{8 304 193 4732 18.5 70 1 10}
{8 360 215 4615 14 70 1 10}
{8 307 200 4376 15 70 1 10}
{8 318 210 4382 13.5 70 1 10}
{8 429 208 4633 11 72 1 10}
{8 400 150 4997 14 73 1 10}
{8 350 180 3664 11 73 1 10}
{8 383 180 4955 11.5 71 1 10}
{8 350 160 4456 13.5 72 1 10}
!!!!!!	PASS	csv	true

-----------------------------------
{:at 4 :hi 5140 :isSorted false :lo 1613 :n 398 :name Lbs- :w -1}
{:at 5 :hi 24.8 :isSorted false :lo 8 :n 398 :name Acc+ :w 1}
{:at 8 :hi 50 :isSorted false :lo 10 :n 398 :name Mpg+ :w 1}
!!!!!!	PASS	data	true

-----------------------------------
50	31.007751937984
!!!!!!	PASS	num	true

-----------------------------------
xmid	{:Clndrs 4.0 :Model 76.0 :Volume 146.0 :origin 1.0}
xdiv	{:Clndrs 1.55 :Model 3.876 :Volume 100.775 :origin 0.775}
ymid	{:Acc+ 15.5 :Lbs- 2800.0 :Mpg+ 20.0}
ydiv	{:Acc+ 2.713 :Lbs- 887.209 :Mpg+ 7.752}
!!!!!!	PASS	stats	true

-----------------------------------
{:div 1.378 :mid a}
!!!!!!	PASS	sym	true

-----------------------------------
{:dump false :eg ALL :file ../data/auto93.csv :help false :nums 512 :seed 10019 :seperator ,}
!!!!!!	PASS	the	true
!!!!!!	PASS	ALL	true
```

### QuickStart

<br/> Clone the repository.
```
git clone https://github.com/vishnuchalla/CSC-510-HW2-Fall22-G41.git
```
<br/> Run the following command to test the test cases.
```
crontab -l
```


### Group 41
1. Vishnu Challa (vchalla2)
2. Sumanth Somasundar (sbangal3)
3. Kanchan Rawat (kprawat)
4. Srujan Ponnur (sponnur)
5. Sairam Sakhamuri (svsakham)
