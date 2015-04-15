# HNDAT
HTTP NTLM Dictionary Attack Tool

A simple python program designed to aid penetration testers in running dictionary attacks against web sites employing HTTP NTLM authentication mechanisms.

Usage is simple:
:~#python ntlmdictauthpy.py http://somewebsite.com/ domainname username-or-user-list-file password-or-password-list-file

Once run, the program will ask you to verify some information and will request you specify a string that indicates an authentication failure (for example the website you are testing may state 'Access is denied' after a failed login attempt).  This information is then used to identify a successful attempt.

Basic multi-threading is included.

I only wrote this because Hydra was giving me some issues.
