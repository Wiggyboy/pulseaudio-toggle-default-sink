# PulseAudio Toggle Default Sink

A small script that easily lets you toggle between default output within PulseAudio with a press of a button.

---
<!---
## Table of contents
* [General info](#general-info)
* [Setup / Installation](#setup-/-installation)
* [Contact](#contact)

---
-->

## General Info
I created the script because I was having two issues with how the default sound devices are handled in Linux (Ubuntu with PulseAudio anyway).

1. When freshly booting, the default audio device is always reset to something I do not use. (Yes I know there was other ways of solving this, but it never worked for me.)
2. Using both a headset and speakers, it's a hassle to open the settings, and change default audio device everytime you switch between the two.

This script was developed to adress both of these issues, and it works flawlessly for me. It should work for you too if you're using PulseAudio.

---

## Dependencies
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Git](https://git-scm.com/) (optional but recommended)

---

## Setup / Installation
| Note: This setup/installation guide is for ubuntu (and debian based distros) mainly. |
| --- |

First install the dependencies starting with [Python 3](https://www.python.org/download/releases/3.0/) (which you probably already). Then we also install [Git](https://git-scm.com/). [Git](https://git-scm.com/) isn't required for the script to work, but will be used during this installation process.

```bash
sudo apt-get update
sudo apt-get install python3

sudo apt-get install git
```

Let's move onto the script download, prefered way using git. Change directory to some prefered place, recommending your home directory.

```bash
cd ~
git clone https://github.com/Wiggyboy/pulseaudio-toggle-default-sink.git
```

Once git has downloaded the script, we'll configure it. In this example we'll use nano as our text editor, but you can use whatever you like.
```bash
cd pulseaudio-toggle-default-sink
nano audio_sinks.py
```

Now we edit the **audio_sinks** at round around line 10 by adding a new lines inside the array. Take help from the comment example in the source code. You can find the names of your audio devices (sinks) by running the script naked (without having configured it).

```bash
python3 audio_sinks.py
```

This will output something along the lines of what you see below. The very bottom the names of your audio devices (sinks) will be printed.
```
audio_sinks cannot be empty.

You probably missed to configure your audio sinks.
Edit audio_sinks.py to fill in the audio_sinks
you would like to be able to toggle through.

Detected possible audio sinks are:
```

Once that is configured, you can try if it works by running the command below.
```bash
python3 toggle_default_sink.py next
python3 toggle_default_sink.py prev
```

Now the script is configured and can be used however you like. However what I recommend is running it once on bootup, which will automatically reapply the default audio device on boot. I also recommend binding the script to a hotkey. I'll show you how to do that too.

So far if you've been running a debian based distro everything should've worked pretty easily, however that's about to change. You'll have to figure out exactly how to setup startup applications yourself if you're not running exactly Ubuntu (19.10) because the guide is getting very specific. However the process will by all likelyhood be very similiar and the **run script command should be almost if not exactly the same**.

Launch the **Startup Applications Preferences** via the **Dash**, click the **Add** button on the top right.
![test image size](/imgs/1.png)

Enter a name and comment to fit you. Then edit and enter the following command, i.e. change **\<user\>** to your linux username, or edit the whole path to where you placed the script in case you didn't go with the home directory.
```bash
python3 /home/<user/pulseaudio-toggle-default-sink/toggle_default_sink.py
```
| Note: In my experience the path has to be exact not relative. <br> I.e. it cannot be `~/pulseaudio-toggle-default-sink/toggle_default_sink.py` |
| --- |

![test image size](/imgs/2.png)

Finally click **Add** to finalize the entry and click **Close**.

Now to the hotkey shortcut. Launch the **Keyboard Shortcuts** via the **Dash**, click the **+ (Plus sign)** button on the very bottom.
![test image size](/imgs/3.png)

Enter a name and choose a shortcut key to fit you. Then edit and enter the following command, i.e. change **\<user\>** to your linux username, or edit the whole path to where you placed the script in case you didn't go with the home directory.
```bash
python3 /home/<user/pulseaudio-toggle-default-sink/toggle_default_sink.py next
```
| Note: In my experience the path has to be exact not relative. <br> I.e. it cannot be `~/pulseaudio-toggle-default-sink/toggle_default_sink.py` |
| --- |

![test image size](/imgs/4.png)

Now, you're all setup! You can try it by hitting your chosen shortcut key. This should toggle through your chosen audio devices (sinks) each time you press.

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright &copy; 2019 Wiggy boy \<Lindholm\>\
  (formally known as Osvald Lindholm)
