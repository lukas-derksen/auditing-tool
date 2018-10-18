# auditing-toolkit
An Open Source auditing tool, developed as proof of concept for my graduation research assignment. 

## Research assignment
The company I work for as an intern wanted me to research the possibility of replacing commercial auditing programs with Open Source tools. Therefore I researched the tools they use, `Acunetix` and `Metasploit Pro`, by looking at their scanresults, documentation and network traffic and by interviewing some of their employees. I then researched what Open Source tooling was available and would come in handy for such a tool. Due to the time I had for this assignment, I chose to use `Python` in development, as it is easy to create powerful tools with in a relatively short time. 

## Tools used in this toolkit

### Nmap
As a reconnaissance tool, I have chosen to use `Nmap`. It has always served me well during CTFs to identify any services that might be interesting for exploitation. During my research, I have seen Metasploit Pro uses it as well to indicate what vulnerabilities might be present within the target. This has lead me to also incorporate `Nmap` into my toolkit. 
