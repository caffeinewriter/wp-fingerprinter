import argparse
import requests # Requires install of Requests: http://python-requests.org/
import re
from urlparse import urlparse

def main():
	parser = argparse.ArgumentParser("Detects WP version from readme.html or meta tag")
	parser.add_argument("-t", "--target", action="append", dest="targets", help="Add a target to scan")

	args = parser.parse_args()

	if args.targets != None:
		scan(args.targets)

def scan(targets):
	for target in targets:
		if not target[:5] == "http:" and not target[:6] == "https:":
			target = "http://" + target
		tltarget = target
		tlurl = urlparse(tltarget)
		target = target + '/readme.html'
		url = urlparse(target)
		r = requests.get(url.geturl())
		if r.status_code != 200:
			t = requests.get(tlurl.geturl())
			w = re.compile(r'<meta name\=\"generator\" content\=\"(WordPress \d+\.\d+\.?(\d+)?)\" \/>', re.I)
			n = w.search(t.text)
			if n:
				print "Site " + tlurl.netloc + tlurl.path + ": Running WordPress " + n.group(1)
			else:
				print "Site " + tlurl.netloc + tlurl.path + ": No version found"
		else:
			v = re.compile(r"Version (\d+\.\d+\.?(\d+)?)", re.I)
			m = v.search(r.text)
			if m:
				print "Site " + tlurl.netloc + tlurl.path + ": Running WordPress " + m.group(1)
			else:
				print "Site " + tlurl.netloc + tlurl.path + ": No version found"

			

if __name__ == "__main__":
	main()

