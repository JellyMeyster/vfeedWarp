# vfeedWarp 0.0.1
vfeed Model and search interface

## What is vfeedWarp
1. vfeed is an opensource correlated cross linked vulnerability database
2. vfeedWarp is a python-peewee wrapper to quickly search the vfeed database (sqlite) for results

## What's in this version?
1. vfeedWarp takes input and fetches the following
    *(a) Throw CPE to get CVE
    *(b) Throw CVE and get CWE or exploitDB id

2. Asking for CWE or exploitDB id is pretty simple. All a user does is alter 
the variables being passed into vfeedWarp. For more details checkout the usage section below.

## Requirements
Running vfeeddWarp required the following:

1. Python 2.7.xx
2. Peewee library
*launch terminal on Linux/Mac or Command Prompt on Windows and run the below command
```
pip install peewee
```
3. Download vfeed from toolswatch

```
git clone https://github.com/toolswatch/vFeed.git
```

4. Download vfeedwarp
```
git clone https://github.com/UShan89/vfeedWarp.git
```

5. Move contents of vfeed into vfeedWarp directory
* Contents of vfeedWarp is now vfeedWarp and vfeed from toolswatch
* The vfeed database is located as "../vfeedWarp/vfeed/vfeed.db

## Using vfeedWarp

Using vfeedWarp is pretty easy. It can be called from python repr 
or on a web-page to throw results. Here is a quick run from python repr.

To Note: 
All return values are list

```
>>> from vfeedWarp import search
>>> search('CVE-2014-2206','cpe')
[u'cpe:/a:getgosoft:getgo_download_manager:4.4.5.502', u'cpe:/a:getgosoft:getgo_download_manager:4.9.0.1982', u'cpe:/a:getgosoft:getgo_download_manager:4.8.2.1346']
>>>
>>> search('cpe:/a:prosody:prosody:0.6.0', 'cve')
[u'CVE-2014-2750', u'CVE-2011-2205', u'CVE-2014-2744', u'CVE-2014-2745']
>>> 
>>> search('CVE-2014-2206', 'cwe')
[u'CWE-119']
>>> search('CVE-2011-1234', 'cwe')
[u'CWE-399']
>>> search('CVE-2014-2206', 'exp')
[u'32132']
>>>
>>> my_product_cves = search('cpe:/a:prosody:prosody:0.6.0', 'cve')
>>> 
>>> for cve in my_product_cves:
...     search(cve, 'cwe')
...
[u'CWE-20']
[u'CWE-399']
[u'CWE-20']
[u'CWE-264']        
>>>
```


## Getting help
To understand the search function, type help(search) in repr
```
>>> from vfeedWarp import search
>>> help(search)
```

## Contributing
Anyone is free to contribute. Checke the LICENSE file if you are making a fork.



