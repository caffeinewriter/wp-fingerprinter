wp-fingerprinter
================

This python application quickly fingerprints WordPress installations, and attempts to grab their version number.

##Usage:

`python wp-fingerprint.py -t target.com -t blog.target.com -t target.com/blog -t https://target.com/blog -t http://blog.target.com`

## Arguments

So far, this only supports a single switch.

`-t, --target` - WordPress installation to attempt and fingerprint. Can be used multiple times in a single execution to iterate through the sites.

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
