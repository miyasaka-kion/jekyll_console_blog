---
title: Visual Studio Code configuration
layout: page
categories:
- cpp
- dev
---

# VSCode: Setting up a Simple C++ Environment

> status: update if needed;
> description: For example, when solving LeetCode problems, you don't need a lot of configuration, a simple environment is sufficient;

## 0x00

First, create a new Profile:

<img src="https://s2.loli.net/2023/09/30/iuvB3K7xUYkzyO5.png" alt="image-20230822170442988" style="width: 50%;">

For example, name it `C++`:

<img src="https://s2.loli.net/2023/09/30/b7ngpYHGEUlMuOf.png" alt="Screenshot 2023-08-22 at 17.05.36" style="width: 50%;">

## 0x01

Install these plugins:

<img src="https://s2.loli.net/2023/09/30/Ht5f83uw19kSsdQ.png" alt="Screenshot 2023-08-22 at 17.09.39" style="width: 50%;">

Whether to use vim is a personal preference; use it if you like:

<img src="https://s2.loli.net/2023/09/30/Dd7JZNFT2hWaxMk.png" alt="Screenshot 2023-08-22 at 17.29.49" style="width: 50%;">

## 0x02

If it warns you, you need to modify the settings for `clangd`;

<img src="https://s2.loli.net/2023/09/30/E8uJjqBCXwP5b3n.png" alt="Screenshot 2023-08-22 at 17.11.05" style="width: 50%;">

Settings:

<img src="https://s2.loli.net/2023/09/30/KzZy4jkTMXcpxIP.png" alt="Screenshot 2023-08-22 at 17.12.21" style="width: 50%;">

Search for `Fallback Flags`:

<img src="https://s2.loli.net/2023/09/30/2WREYStPm9K7ZpB.png" alt="Screenshot 2023-08-22 at 17.12.49" style="width: 50%;">

Add a standard you like:

<img src="https://s2.loli.net/2023/09/30/zT7EG8C3lsx1W6M.png" alt="Screenshot 2023-08-22 at 17.13.45" style="width: 50%;">

Restart VSCode, and the warning will disappear;

<img src="https://s2.loli.net/2023/09/30/rNnTSXQFI3jZGx2.png" alt="Screenshot 2023-08-22 at 17.15.20" style="width: 50%;">

## 0x03

Press `Ctrl + Option + N` to run the code:

<img src="Users/kion/Desktop/Screenshot 2023-08-22 at 17.16.54.png" alt="Screenshot 2023-08-22 at 17.16.54" style="width: 50%;">

By default, Code Runner does not use the `-std=c++__` argument, you can add this to avoid warnings:

Settings:

<img src="https://s2.loli.net/2023/09/30/BRCybg6ATFzQOGU.png" alt="Screenshot 2023-08-22 at 17.20.29" style="width: 50%;">

Click on `Edit in settings.json` or use `Shift + Command + P` to search for `settings.json`;

<img src="https://s2.loli.net/2023/09/30/Ytmn1zaUBxpAKSg.png" alt="Screenshot 2023-08-22 at 17.23.17" style="width: 50%;">

Search for `cpp`:

<img src="https://s2.loli.net/2023/09/30/dKbtavsEOnV7jL3.png" alt="Screenshot 2023-08-22 at 17.26.42" style="width: 50%;">

Add `-std=c++14` or your desired version after `g++`:

<img src="https://s2.loli.net/2023/09/30/U4YzjufMVwevnlm.png" alt="Screenshot 2023-08-22 at 17.27.54" style="width: 50%;">

Save and exit;

<img src="https://s2.loli.net/2023/09/30/9W4FdR1cSxPubfK.png" alt="Screenshot 2023-08-22 at 17.28.35" style="width: 50%;">

It won't show warnings anymore.

## 0xff

Finally, here's a quirky picture:

<img src="https://s2.loli.net/2023/09/30/MNCV1TxP7ibprhH.png" alt="Screenshot 2023-08-20 at 02.31.10" style="width: 50%;">