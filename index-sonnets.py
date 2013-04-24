import sys
import os
import errno
from contextlib import closing

import xapian as _x

def main(files):
    # try to make a db in pwd
    try:
        os.mkdir('./xdb/')
    except (OSError, IOError), e:
        if e.errno != errno.EEXIST:
            raise

    with closing(_x.WritableDatabase('./xdb/sonnets.db',
                                     _x.DB_CREATE_OR_OPEN)) as x_db:
        # setup our indexer
        for f in files:
            with closing(open(f, 'r+')) as f:
                sonnet = f.read()
                num_lines = len(sonnet.split('\n'))
                author = 'William Shakespeare'

                # make a new document
                x_doc = _x.Document()

                # set sonnet text as data, and name as id
                x_id = 'Q%s' % f.name
                x_doc.set_data(sonnet)
                x_doc.add_term(x_id)

                # setup indexer
                indexer = _x.TermGenerator()
                indexer.set_stemmer(_x.Stem("english"))
                indexer.set_document(x_doc)

                # make author searchable in main text
                indexer.index_text(author)
                # do not keep going from author to text, seperate them
                indexer.increase_termpos()
                # index author into 'A' prefix, seperately
                indexer.index_text(author, 1, 'A')

                # index sonnet text
                indexer.index_text(sonnet)

                # add XLINES as number of lines
                x_doc.add_term('XLINES%s' % num_lines)

                # save
                x_db.replace_document(x_id, x_doc)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
