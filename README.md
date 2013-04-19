<h1>Directory Finder</h1>
Written in Python, this script searches for a particular file or directory using a word list
If two word lists are specified, urls will be generated with every combination
All valid URLs are written to standard error
<h2>Example</h2>
apple-apple
apple-banana
apple-carrot
banana-apple
banana-banana
banana-carrot
...

Usage: Single List
``
python DirectoryFinder.py [wordlist] [url prefix] 2> valid.txt
``
Usage: Dual List
``
python DirectoryFinder.py [wordlist1] [wordlist2] [url prefix] 2> valid.txt
``
