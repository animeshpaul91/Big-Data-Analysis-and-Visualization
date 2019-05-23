from glob import glob
import warc
import eventlet
eventlet.monkey_patch()

topics = ['baseball', 'basketball', 'rugby', 'football']

for topic in topics:
    warc_file = './' + topic + '/' + topic + '.warc.gz'
    url_file = './' + topic + '/' + topic + '_urls.txt'
    warc_files = glob(warc_file)
    f1 = open(url_file, 'a+')
    for fn in warc_files:
        f = warc.open(fn)
        for record in f:
            url = record.header.get('warc-target-uri', None)
            if url is not None:
                f1.write(url + '\n')
    f1.close()
