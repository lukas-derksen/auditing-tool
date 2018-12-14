import subprocess

# Change to location of fuzzdb
fuzzdb = '/home/lukas/Documents/School/Afstuderen/gitrepos/fuzzdb'

def initiate(host):
    scan = subprocess.Popen(["whatweb", host], stdout=subprocess.PIPE)
    analyze(scan.communicate())

def analyze(data):
    lines = data[0].split(b', ')
    for line in lines:
        line = line.decode('ascii').lower()
        print(line)
        with open('/tmp/wordlist', 'w') as wordlist:
            with open('{0}/discovery/predictable-filepaths/filename-dirname-bruteforce/raft-large-files-lowercase.txt'.format(fuzzdb), 'r', encoding = "ISO-8859-1") as current:
                append_lines(current, wordlist)
            if 'apache' in line:
                # Add apache specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/Apache.txt'.format(fuzzdb), 'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'axis' in line:
                # Add apache axis specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/Apache_Axis.txt'.format(fuzzdb), 'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'tomcat' in line:
                # Add apache tomcat specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/ApacheTomcat.txt'.format(fuzzdb), 'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'jboss' in line:
                # Add JBoss specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/JBoss.txt'.format(fuzzdb), 'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'joomla' in line:
                # Add Joomla specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/Joomla_exploitable.txt'.format(fuzzdb), 'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'iis' in line:
                # Add IIS specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/IIS.txt'.format(fuzzdb),'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'hyperion' in line:
                # Add hyperion specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/Hyperion.txt'.format(fuzzdb),'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'jrun' in line:
                # Add jrun specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/Jrun.txt'.format(fuzzdb),'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if any(x in line for x in ['active directory', 'adfs', 'active', 'directory']):
                # Add adfs specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/ADFS.txt'.format(fuzzdb),'r', encoding = "ISO-8859-1") as current:
                    append_lines(current, wordlist)
            if 'oracle' in line:
                # Add oracle specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/Oracle9i.txt'.format(fuzzdb),'r', encoding = "ISO-8859-1") as current:
                    append_lines(current,wordlist)
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/OracleAppServer.txt'.format(fuzzdb),'r', encoding = "ISO-8859-1") as current:
                    append_lines(current,wordlist)
            if 'sap' in line:
                # Add SAP specific words to wordlist
                with open('{0}/discovery/predictable-filepaths/webservers-appservers/SAP.txt'.format(fuzzdb),'r', encoding = "ISO-8859-1") as current:
                    append_lines(current,wordlist)

def append_lines(read, write):
    write.writelines(read.readlines())