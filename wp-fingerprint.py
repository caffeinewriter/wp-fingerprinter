import argparse
import requests # Requires install of Requests: http://python-requests.org/
import re
from urlparse import urlparse

def main():
	parser = argparse.ArgumentParser("Detects WP version from readme.html or meta tag")
	parser.add_argument("-t", "--target", action="append", dest="targets", help="Add a target to scan")
	parser.add_argument("-u", "--user-agent", action="store", dest="ua", help="A custom UA string to use in requests to the server")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="Turn on verbose mode. Useful for seeing the details of errors")

	args = parser.parse_args()

	if args.targets != None:
		scan(args.targets, args.verbose, args.ua)

def scan(targets, verbose, ua):
	for target in targets:
		if not target[:5] == "http:" and not target[:6] == "https:":
			target = "http://" + target
		tltarget = target
		tlurl = urlparse(tltarget)
		target = target + '/readme.html'
		url = urlparse(target)
		try:
			if not ua:
				r = requests.get(url.geturl())
			else:
				r = requests.get(url.geturl(), headers={'User-Agent': ua})
		except requests.exceptions.ConnectionError, e:
			print "Error: Unable to connect to " + tlurl.netloc
			if verbose:
				print e
		else:
			if r.status_code != 200:
				if not ua:
					t = requests.get(tlurl.geturl())
				else:
					t = requests.get(tlurl.geturl(), headers={'User-Agent': ua})
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

