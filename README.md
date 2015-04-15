# HNDAT
HTTP NTLM Dictionary Attack Tool

A simple python program designed to aid penetration testers in running dictionary attacks against web sites employing HTTP NTLM authentication mechanisms.

Usage is simple:
:~#python hndat.py http://somewebsite.com/ domainname username-list-file password-list-file

Once run, the program will ask you to verify some information and will request you specify a string that indicates an authentication failure (for example the website you are testing may state 'Access is denied' after a failed login attempt).  This information is then used to identify a successful attempt. HTTP or HTTPS works.

Basic multi-threading is included.

I only wrote this because Hydra was giving me some issues.
