# Auditing Toolkit
An Open Source auditing tool, developed as proof of concept for my graduation research assignment. 

## Research assignment
The company I work for as an intern wanted me to research the possibility of replacing commercial auditing programs with Open Source tools. Therefore I researched the tools they use, `Acunetix` and `Metasploit Pro`, by looking at their scanresults, documentation and network traffic and by interviewing some of their employees. I then researched what Open Source tooling was available and would come in handy for such a tool. Due to the time I had for this assignment, I chose to use `Python` in development, as it is easy to create powerful tools with in a relatively short time. 

## Tools used in this toolkit

### Network audit tool

#### Nmap
As a reconnaissance tool, I have chosen to use `Nmap`. It has always served me well during CTFs to identify any services that might be interesting for exploitation. During my research, I have seen Metasploit Pro uses it as well to indicate what vulnerabilities might be present within the target. This has lead me to also incorporate `Nmap` into my toolkit. 

#### Metasploit
Once `Nmap` has retrieved details about the target, the tool will look for exploits using `Metasploit`. These will be automatically executed, as to confirm if the services are truly vulnerable. This will all be logged within the terminal and will also be written in the `Markdown` report afterwards. 

### Webapp audit tool

#### Whatweb
`Whatweb` is a tool that scans the website for wellknown services, such as `http` server (e.g. `Apache`), `cms` (e.g. `WordPress`), Operating System (e.g. `Ubuntu`). This information will be used in further scans, by searching specific wordlists with words that are commonly found in those systems (for instance the server status page in `Apache` or the `wp-admin.php` page in `wordpress`).

#### Dirb
`Dirb`, short for Directory Buster, is a commandline tool which will use above mentioned wordlists to index all files it can find on a `domain`. It does so by `bruteforcing` the `url` of the site, adding each word in the wordlist behind the given `url`. 

#### FuzzDB
`FuzzDB` is not a tool, but a directory full of wordlists with common `passwords`, `usernames`, filenames, pages, et cetera. 

#### Owasp ZAProxy

_More to come_