#!/bin/bash


cliPackages=" 
  btop zsh ranger screen git micro 
  podman python nodejs npm yay fastfetch 
  iwd impala
"


niriPackages="
  niri xwayland-satellite xdg-desktop-portal-gnome 
  xdg-desktop-portal-gtk alacritty cava qt6-multimedia-ffmpeg
"


utils="
  mako rofi nemo qt6ct kvantum
  nwg-look nirimod-git 
"


vscodeGit="code-git"


# Oh My Zsh install
# sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


# Run IWD and Impala
# sudo systemctl stop NetworkManager
# sudo systemctl disable NetworkManager
# sudo systemctl enable --now iwd