Sonnets Xapian Demo
-------------------

    @author: Matt Story <matt.story@axial.net>
    @license: BSD 3-Clause (see LICENSE)

The Slides
----------

The Sonnets Xapian Demo was built for the
[Getting Started with Python and Xapian -- HackNY](https://docs.google.com/presentation/d/1G1c-5hRLDWSSgy8moL2vJ_SWdk9yvJdZNF8ERYn3ZlI/edit?usp=sharing)
[HackNY](http://hackny.org) Spring Student Hackathon, where I participated as
a [tech ambassador](https://www.hackerleague.org/hackathons/spring-2013-hackny-student-hackathon/wikipages/515dfd78baf81d677300005d)
(although the talk was not given due to room difficulties).

The Sonnets
-----------

The sonnets were taken by hand from
[here](http://www.gutenberg.org/ebooks/1041.txt.utf-8),
and parsed.  This content is available freely under the public domain in the
USA.

The Demos
---------

### index-sonnets.py

`index-sonnets.py` takes an list of files to index on the command-line:

    $ python index-sonnets.py sonnets/1 sonnets/2 # etc ...

And indexes them with the author 'William Shakespeare' to the database
`./xdb/sonnets.db`.  To index all the sonnets:

    $ find shakespeare/ -type f  | xargs python index-sonnets.py

### search-sonnets.py

`query-sonnets.py` takes a query string as its first argument, an optional
author query string for its second argument and optionally number of lines in
the sonnet as its third argument (admittedly a terrible interface, but it's a
demo ...).  Some things you can try:

    $ python query-sonnets.py 'shall'
    $ python query-sonnets.py 'shall' '' 15
    $ python query-sonnets.py '' '' 16
