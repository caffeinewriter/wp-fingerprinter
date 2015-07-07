wp-fingerprinter
================

This python application quickly fingerprints WordPress installations, and attempts to grab their version number.

##Usage:

`python wp-fingerprint.py -t target.com -t blog.target.com -t target.com/blog -t https://target.com/blog -t http://blog.target.com -u="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/43.0.2357.124 Safari/537.36" -v`

## Arguments

`-t, --target` - WordPress installation to attempt and fingerprint. Can be used multiple times in a single execution to iterate through the sites.

`-u, --user-agent` - Sets a custom user agent to be used in the requests.

`-v, --verbose` - Will spit out error details. More to come on this in the future.

## Building

Make sure to install dependencies. 

```
pip install -r requirements.txt
```

Or you can install dependencies manually.

```
pip install requests pyinstaller
```

This has been successfully built with `pyinstaller`.

```
#First line not necessary if you ran the dependency install command
pip install pyinstaller
pyinstaller -F wp-fingerprintpy
````
