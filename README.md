# Bit & Packet Error Loss

GitHub repository: https://github.com/elopezga/python-ivi.git

Have a question or find a problem? Email me at: elopezga@ucsd.edu

# Introduction

This repository contains the tools to be able to run bit error and packet error
analysis used by the paper: Measuring Bit Error and Packet Error with Python.

Link to Paper:

Note that some dependencies are not included in this repository, but are linked
with their latest versions.

# Dependencies
Scapy: http://www.secdev.org/projects/scapy/ (2.3.1 used)

matplotlib: https://github.com/matplotlib/matplotlib.git

Python-IVI: Included in this repository

Wireshark: https://www.wireshark.org/download.html

# How To Use:
This repository contains the Python-IVI drivers to connect to various lab equipment
in a network. It also contains core python modules to measure Bit Error and Packet Error.

At a high-level, you will use the Python-IVI drivers to connect to the your experiment setup
to access equipment, such as attenuators or OSA, to automate settings in the equipment via
a python script. Once you gain automation control of the lab equipment, you begin specifiying
your experiment details, such as stating which equipment settings change (e.g. changing
attenuation setting in steps over the experiment). These should usually go in a loop so that
at each loop iteration the settings get incemented by a step value. Within this loop, you
want to call the bit/packet analyzing modules. These include: RunForErrors, RunErrors,
RunTrail. These all have slightly different functionality in how they called and how they
collect packets.

The bit/packet analysis modules in LivePCAPReader.py reads packets with tshark (included with wireshark), creates
a pcap filed with these packets, and opens it for analysis. The analysis result is then
recorded in the DataContainer class. You can output this data to csv using its writeToFile
method (Note that the RunTrails method already does this for you).

An experiment script has been included as /ErrorRate/crosstalkpacketloss.py. This script
make it more clear how the different components provided by this repository interact with
each other to produce bit/packet error.