# NEO
## Brain meets Google Assistant

* bridging a muse headband to google's open source voice assistant
* recieve active voice feedback from the assistant during your muse meditation session (+ ability to control VA w/ muse)
* stream muse data (OSC format) using Muse SDK
* recieve stream from python pyliblo based server on Rpi w/ voice shield

# Required Technologies

* Muse Headband (Muse V2)
* Muse Direct (SDK for windows 10) With CSR8510 Bluetooth 4.0 USB Dongle (Or another OSC compliant streaming server)
* Google AIY Voice Kit (Raspberry Pi Zero WH + Voice Bonnet Shield)
* AIY + PyLiblo library for Python 3.5+

# How to Run

* Install [Muse Direct](http://developer.choosemuse.com/tools/windows-tools/musedirect)
* Install AIY Voice and [PyLiblo](https://github.com/dsacre/pyliblo) for python 3.5+
* clone repo ``` git clone https://github.com/Ayuzer/Neo.git ```

* ```cd ``` to ``` Neo ```
* cd to ``/Neo`` and run ``./environment.bash``
* run `` Neo.py `` from Raspberry Pi to start local server that listens for data from Muse


