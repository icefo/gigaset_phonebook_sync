# gigaset_phonebook_sync
I coded this to improve my gigaset c610ip system.
By default when you add or delete a number with an handset, the changes are not replicated to the other handsets and... It sucks.
This script add a sync function and is supposed to be run as a cron job every night. I advise you to run this at night because the script need 4-5 minutes to complete and should not be interrupted.
It currently work with 3 handsets but it can be easily changed to fit your configuration.

I'll be honest here : the script work 90% of the time and the code is utter crap. It would probably be way better if I knew some js (the webinterface is full of it) but sadly I dont. So I used selenium to pull/push the phonebooks from/to the phones and selenium is not really suited for that.

It took me 3 days to get this working and I can't see it anymore. So if you want me to make it work better, just open an issue. It would give me some motivation.

Have a good day :-)
