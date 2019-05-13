#!/bin/bash
hugo -d ~/Downloads/cpbotha.net
# sync contents of public dir into static_cpbothanet/
# don't add --delete, you always lose stuff you did not intend to lose! (last time .htaccess)
#
# rsync info config will give us single updated line of progress; and stats at the end!
rsync --info=progress2,stats1 -a --exclude=.htaccess --exclude=pcdc --exclude=files --exclude=thingies ~/Downloads/cpbotha.net/ cpbotha@cpbotha.webfactional.com:~/webapps/static_cpbothanet

# funny thing: on windows, both wsl and powershell, the scroll buffer gets
# full, and then the rsync will stop, and then you have to resize the window
# multiple times to finish the transfer. The info config helps with this!
