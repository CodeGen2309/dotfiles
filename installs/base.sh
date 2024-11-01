#! /bin/bash
# just test

# SINGLE APPS
packgs="
webapp-manager
code
obsidian
vivaldi
flatpak
qbittorrent
python-pillow
zoom
git
otf-font-awesome
"


#NODE JS
packgs+="
nodejs
npm
"

#DOCKER
packgs+="
docker
docker-compose
"

#CONSOLE UTILS
packgs+="
kitty
ranger
micro
atool
"


pamac install $packgs


flatlist="
org.onlyoffice.desktopeditors
com.anydesk.Anydesk
com.getpostman.Postman
com.google.Chrome
ru.yandex.Browser
"

flatpak install $flatlist
