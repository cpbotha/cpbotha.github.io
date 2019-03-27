#!/bin/bash

hugo -d ~/Downloads/cpbotha.net
# sync contents of public dir into static_cpbothanet/
rsync -av --progress --delete --exclude=pcdc --exclude=files --exclude=thingies ~/Downloads/cpbotha.net/ cpbotha@cpbotha.webfactional.com:~/webapps/static_cpbothanet
