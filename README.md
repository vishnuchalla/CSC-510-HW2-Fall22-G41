# CSC-510-HW2-Fall22-G41
Homework Repo for Software Engineering 22 Group 41

[![Build Status](https://app.travis-ci.com/vishnuchalla/CSC-510-HW2-Fall22-G41.svg?branch=main)](https://app.travis-ci.com/vishnuchalla/CSC-510-HW2-Fall22-G41)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7053897.svg)](https://doi.org/10.5281/zenodo.7053897)
[![Code Coverage](https://codecov.io/github/vishnuchalla/CSC-510-HW2-Fall22-G41/branch/main/graph/badge.svg?token=AJ0WMF1F1J)](https://codecov.io/github/vishnuchalla/CSC-510-HW2-Fall22-G41)

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
{'eg': 'ALL', 'dump': False, 'file': './data/auto93.csv', 'help': False, 'nums': 512, 'seed': 10019, 'seperator': ','}
-----------------------------------
TestNum:test_add_elifblock
TestNum:test_add_if_block
TestNum:test_div
TestNum:test_mid
TestNum:test_num
TestNum:test_nums_false_case
TestNum:test_nums_true_case
TestNum:test_per
TestPrettyPrint:test_bigNum
TestPrettyPrint:test_oo
TestPrettyPrint:test_the
TestSym:test_add
TestSym:test_div
TestSym:test_mid
TestSym:test_sym
TestData:test_data
TestData:test_stats
TestCsv:test_csv
-----------------------------------
-----------------------------------
TestNum:test_add_elifblock - PASSED
-----------------------------------
-----------------------------------
TestNum:test_add_if_block - PASSED
-----------------------------------
-----------------------------------
TestNum:test_div - PASSED
-----------------------------------
-----------------------------------
TestNum:test_mid - PASSED
-----------------------------------
-----------------------------------
50 31.007751937984494
TestNum:test_num - PASSED
-----------------------------------
-----------------------------------
TestNum:test_nums_false_case - PASSED
-----------------------------------
-----------------------------------
TestNum:test_nums_true_case - PASSED
-----------------------------------
-----------------------------------
TestNum:test_per - PASSED
-----------------------------------
-----------------------------------
OrderedDict([(3, 3), (6, 6), (10, 10), (11, 11), (16, 16), (17, 17), (18, 18), (22, 22), (24, 24), (27, 27), (28, 28), (33, 33), (35, 35), (39, 39), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (51, 51), (52, 52), (53, 53), (54, 54), (59, 59), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (69, 69), (70, 70), (72, 72), (74, 74), (75, 75), (76, 76), (79, 79), (81, 81), (84, 84), (86, 86), (87, 87), (89, 89), (93, 93), (94, 94), (95, 95), (97, 97), (98, 98), (99, 99), (100, 100), (102, 102), (103, 103), (104, 104), (105, 105), (107, 107), (108, 108), (109, 109), (113, 113), (115, 115), (116, 116), (119, 119), (120, 120), (121, 121), (122, 122), (123, 123), (124, 124), (125, 125), (127, 127), (128, 128), (129, 129), (130, 130), (131, 131), (132, 132), (133, 133), (136, 136), (137, 137), (138, 138), (139, 139), (141, 141), (142, 142), (144, 144), (146, 146), (150, 150), (154, 154), (157, 157), (159, 159), (161, 161), (162, 162), (165, 165), (166, 166), (168, 168), (170, 170), (173, 173), (174, 174), (179, 179), (181, 181), (183, 183), (184, 184), (185, 185), (186, 186), (189, 189), (194, 194), (195, 195), (197, 197), (199, 199), (200, 200), (201, 201), (202, 202), (203, 203), (204, 204), (205, 205), (206, 206), (207, 207), (208, 208), (209, 209), (210, 210), (211, 211), (212, 212), (213, 213), (216, 216), (219, 219), (222, 222), (226, 226), (227, 227), (230, 230), (236, 236), (241, 241), (243, 243), (244, 244), (245, 245), (247, 247), (254, 254), (261, 261), (262, 262), (263, 263), (265, 265), (266, 266), (268, 268), (269, 269), (271, 271), (272, 272), (274, 274), (275, 275), (276, 276), (277, 277), (278, 278), (279, 279), (282, 282), (283, 283), (284, 284), (289, 289), (290, 290), (291, 291), (294, 294), (298, 298), (299, 299), (301, 301), (302, 302), (303, 303), (305, 305), (307, 307), (310, 310), (312, 312), (314, 314), (319, 319), (321, 321), (324, 324), (325, 325), (326, 326), (328, 328), (332, 332), (333, 333), (337, 337), (339, 339), (341, 341), (343, 343), (346, 346), (347, 347), (348, 348), (351, 351), (354, 354), (356, 356), (358, 358), (359, 359), (360, 360), (361, 361), (363, 363), (365, 365), (369, 369), (371, 371), (372, 372), (373, 373), (374, 374), (376, 376), (380, 380), (382, 382), (383, 383), (386, 386), (389, 389), (393, 393), (394, 394), (395, 395), (399, 399), (402, 402), (404, 404), (406, 406), (407, 407), (410, 410), (412, 412), (416, 416), (420, 420), (421, 421), (423, 423), (424, 424), (425, 425), (427, 427), (428, 428), (431, 431), (433, 433), (434, 434), (435, 435), (436, 436), (437, 437), (442, 442), (443, 443), (447, 447), (448, 448), (451, 451), (455, 455), (456, 456), (462, 462), (464, 464), (466, 466), (468, 468), (471, 471), (473, 473), (474, 474), (475, 475), (476, 476), (480, 480), (482, 482), (485, 485), (486, 486), (489, 489), (490, 490), (493, 493), (494, 494), (495, 495), (497, 497), (500, 500), (501, 501), (502, 502), (504, 504), (505, 505), (506, 506), (508, 508), (511, 511), (512, 512), (242, 513), (267, 514), (259, 519), (398, 520), (390, 523), (55, 527), (509, 528), (110, 532), (281, 533), (224, 534), (286, 536), (264, 540), (377, 542), (499, 543), (240, 544), (453, 547), (357, 548), (392, 549), (296, 550), (449, 551), (334, 552), (152, 553), (112, 554), (231, 555), (153, 559), (496, 560), (239, 561), (7, 562), (40, 572), (15, 573), (439, 575), (20, 576), (288, 577), (280, 581), (293, 582), (140, 583), (381, 588), (387, 589), (223, 590), (169, 593), (5, 595), (214, 597), (232, 599), (14, 602), (19, 603), (306, 605), (349, 607), (488, 610), (411, 611), (396, 612), (311, 614), (80, 616), (34, 618), (327, 619), (256, 620), (422, 621), (255, 625), (318, 626), (60, 627), (487, 628), (172, 630), (403, 633), (176, 634), (355, 636), (260, 638), (484, 639), (246, 640), (134, 643), (477, 646), (432, 648), (251, 649), (31, 650), (111, 652), (25, 653), (270, 654), (415, 657), (316, 659), (252, 662), (118, 663), (85, 664), (164, 666), (198, 669), (297, 670), (2, 671), (62, 672), (249, 673), (88, 676), (414, 677), (459, 678), (156, 681), (461, 684), (158, 686), (367, 689), (366, 690), (257, 691), (498, 694), (258, 699), (41, 701), (78, 703), (287, 704), (322, 705), (58, 707), (217, 708), (397, 710), (48, 711), (292, 712), (4, 714), (114, 715), (73, 717), (68, 718), (151, 725), (364, 727), (491, 732), (96, 733), (479, 738), (440, 740), (454, 741), (192, 742), (463, 745), (467, 746), (295, 747), (178, 748), (71, 752), (458, 753), (117, 754), (175, 755), (409, 756), (8, 758), (82, 759), (196, 760), (413, 761), (503, 762), (446, 763), (375, 764), (469, 765), (148, 767), (101, 768), (438, 771), (9, 772), (408, 773), (320, 774), (470, 775), (344, 778), (391, 781), (362, 782), (285, 784), (460, 791), (233, 792), (90, 794), (465, 796), (220, 797), (42, 800), (335, 801), (273, 806), (143, 807), (309, 808), (1, 810), (188, 812), (450, 814), (250, 817), (248, 818), (91, 821), (221, 824), (83, 826), (135, 828), (379, 829), (26, 831), (191, 832), (215, 833), (106, 834), (430, 837), (378, 841), (160, 843), (126, 845), (405, 847), (167, 849), (77, 850), (481, 852), (228, 856), (483, 857), (253, 858), (304, 862), (388, 863), (30, 864), (187, 866), (29, 867), (50, 868), (385, 869), (234, 870), (36, 877), (342, 878), (57, 883), (313, 884), (429, 891), (350, 894), (235, 895), (507, 897), (145, 898), (147, 900), (180, 902), (163, 904), (353, 905), (445, 906), (61, 911), (441, 912), (12, 915), (384, 916), (237, 917), (478, 919), (317, 921), (419, 922), (229, 924), (331, 925), (401, 927), (13, 928), (457, 930), (23, 932), (400, 933), (336, 934), (182, 935), (340, 936), (32, 937), (155, 939), (177, 940), (444, 942), (452, 945), (190, 949), (193, 952), (426, 954), (315, 955), (225, 959), (370, 962), (323, 963), (368, 964), (38, 969), (171, 970), (330, 972), (472, 973), (238, 974), (418, 975), (49, 977), (308, 979), (300, 980), (510, 981), (92, 985), (21, 986), (345, 987), (37, 988), (149, 989), (352, 990), (338, 994), (417, 995), (56, 997), (492, 998), (218, 999), (329, 1000)])
TestPrettyPrint:test_bigNum - PASSED
-----------------------------------
-----------------------------------
{:dump False :eg ALL :file ./data/auto93.csv :help False :nums 512 :seed 10019 :seperator ,}
TestPrettyPrint:test_oo - PASSED
-----------------------------------
-----------------------------------
{:dump False :eg ALL :file ./data/auto93.csv :help False :nums 512 :seed 10019 :seperator ,}
TestPrettyPrint:test_the - PASSED
-----------------------------------
-----------------------------------
TestSym:test_add - PASSED
-----------------------------------
-----------------------------------
TestSym:test_div - PASSED
-----------------------------------
-----------------------------------
TestSym:test_mid - PASSED
-----------------------------------
-----------------------------------
{:div 1.378 :mid a}
TestSym:test_sym - PASSED
-----------------------------------
-----------------------------------
{:at 3 :hi 5140 :isSorted False :lo 1613 :n 398 :name Lbs- :w -1}
{:at 4 :hi 24.8 :isSorted False :lo 8 :n 398 :name Acc+ :w 1}
{:at 7 :hi 50 :isSorted False :lo 10 :n 398 :name Mpg+ :w 1}
TestData:test_data - PASSED
-----------------------------------
-----------------------------------
xmid {:Clndrs 4.0 :Model 76.0 :Volume 146.0 :origin 1.0}
xdiv {:Clndrs 1.55 :Model 3.876 :Volume 100.775 :origin 1.327}
ymid {:Acc+ 15.0 :Lbs- 2800.0 :Mpg+ 20.0}
ydiv {:Acc+ 2.713 :Lbs- 887.209 :Mpg+ 7.752}
TestData:test_stats - PASSED
-----------------------------------
-----------------------------------
{Clndrs Volume Hp: Lbs- Acc+ Model origin Mpg+}
{8 304.0 193 4732 18.5 70 1 10}
{8 360 215 4615 14 70 1 10}
{8 307 200 4376 15 70 1 10}
{8 318 210 4382 13.5 70 1 10}
{8 429 208 4633 11 72 1 10}
{8 400 150 4997 14 73 1 10}
{8 350 180 3664 11 73 1 10}
{8 383 180 4955 11.5 71 1 10}
{8 350 160 4456 13.5 72 1 10}
TestCsv:test_csv - PASSED
-----------------------------------
--------------Summary--------------
18 PASSED 		0 FAILED 
Success Rate:- 100.0%		Failure Rate:- 0.0%

```

### QuickStart

<br/> Clone the repository.
```
git clone https://github.com/vishnuchalla/CSC-510-HW2-Fall22-G41.git
```
<br/> Install the required packages.
```
pip install -r requirements.txt
```
<br/> Run the following command to run the test cases.
```
python3 test/Framework.py
```


### Group 41
1. Vishnu Challa (vchalla2)
2. Sumanth Somasundar (sbangal3)
3. Kanchan Rawat (kprawat)
4. Srujan Ponnur (sponnur)
5. Sairam Sakhamuri (svsakham)
