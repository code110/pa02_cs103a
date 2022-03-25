# PA02_cs103a
### Collaborators:
Junhao Wang\
Zihao Liu \
Tingwei Liu 

### Instructor:
Tim Hickey 

typescript recording:

Script started on Thu Mar 24 22:23:14 2022
```ls```
(base) zach@MacBook-Pro pa02_cs103a % ls
README.md           category.py         test_category.py    tracker.db          transactions.py
__pycache__         pytest.ini          test_transaction.py tracker.py          typescript
(base) zach@MacBook-Pro pa02_cs103a % pylint transactions.py 
************* Module transactions
transactions.py:44:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:52:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:65:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:88:81: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:100:77: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:111:76: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:22:0: C0115: Missing class docstring (missing-class-docstring)
transactions.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:54:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:67:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:76:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:85:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:97:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:108:4: C0116: Missing function or method docstring (missing-function-docstring)
------------------------------------------------------------------
Your code has been rated at 7.65/10 (previous run: 7.65/10, +0.00)

```pytest -v test_transaction.py```
(base) zach@MacBook-Pro pa02_cs103a % pytest -v test_transaction.py 
======================================================================= test session starts ========================================================================
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /Users/zach/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/zach/pa02_cs103a, configfile: pytest.ini
plugins: anyio-2.2.0
collected 6 items                                                                                                                                                  

test_transaction.py::test_add PASSED                                                                                                                         [ 16%]
test_transaction.py::test_delete PASSED                                                                                                                      [ 33%]
test_transaction.py::test_sum_date PASSED                                                                                                                    [ 50%]
test_transaction.py::test_sum_month PASSED                                                                                                                   [ 66%]
test_transaction.py::test_sum_year PASSED                                                                                                                    [ 83%]
test_transaction.py::test_sum_cat PASSED                                                                                                                     [100%]

======================================================================== 6 passed in 0.05s =========================================================================
(base) zach@MacBook-Pro pa02_cs103a % python tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 1
id  name       description                   
---------------------------------------------
1   1          test                          
> 2
category name: food
category description: food cat 
> 1
id  name       description                   
---------------------------------------------
1   1          test                          
2   food       food cat                      
> 5
amount: 1000
category: food
date: 2022-09-27
description: food 1000
> 4


item #     amount     category   date            description                   
------------------------------------------------------------
1          10000      food       2011-09-28      test                          
2          200        textbook   2022-09-21      test2                         
3          200        food       2022-09-30      test3                         
4          300        textbook   2011-09-28      test4                         
5          1000       food       2022-09-27      food 1000                     
> 6      
rowid: 3
> 4


item #     amount     category   date            description                   
------------------------------------------------------------
1          10000      food       2011-09-28      test                          
2          200        textbook   2022-09-21      test2                         
4          300        textbook   2011-09-28      test4                         
5          1000       food       2022-09-27      food 1000                     
> 7
sum        date      
---------------------------------------------
10300      2011-09-28
200        2022-09-21
1000       2022-09-27
> 8
sum        month     
---------------------------------------------
1200       2022-09   
10300      2011-09   
> 9
sum        year      
---------------------------------------------
10300      2011      
1200       2022      
> 10
sum        category  
---------------------------------------------
11000      food      
500        textbook  
> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> exit
invalid choice
> exit()
invalid choice
> exit
invalid choice
> ls  
invalid choice
> 0
bye
(base) zach@MacBook-Pro pa02_cs103a % exit

Script done on Thu Mar 24 22:29:16 2022
