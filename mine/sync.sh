hugo -d ~/Downloads/cpbotha.net

echo "HUGO DONE"

# sync contents of public dir into static_cpbothanet/
# don't add --delete, you always lose stuff you did not intend to lose! (last time .htaccess)
#
# rsync info config will give us single updated line of progress; and stats at the end!
rsync --info=progress2,stats1 -a --exclude=.htaccess --exclude=pcdc --exclude=files --exclude=thingies ~/Downloads/cpbotha.net/ cpbotha@cpbotha.webfactional.com:~/webapps/static_cpbothanet

# funny thing: on windows, both wsl and powershell, the scroll buffer gets
# full, and then the rsync will stop, and then you have to resize the window
# multiple times to finish the transfer. The info config helps with this!

# this also happens when running /bin/bash from Emacs term.el
# and it even happens when I redirect output to a file.
# prepending stdbuf -o0 also does not help

# FRUSTRATING. I can run the rsync command by itself. progress output looks
# different (percentage not updating), but it runs to completion.
