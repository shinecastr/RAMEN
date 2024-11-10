# RAMEN

## Ryan's Awesome Multi-Effects Node

RAMEN is an open music technology project created for my Music and Sound Recording Capstone for the University of New Haven. 

RAMEN relies on [Patchbox OS 2024-04-04](https://community.blokas.io/t/beta-patchbox-os-bookworm-arm64-2024-04-04/5163) and PureData Vanilla 0.53

## Build Your Own

### Componenents

- Raspberry Pi 5 8 GB
- HiFiBerry DAC2 ADC Pro
- Pimoroni NVMe Base
- NVMe SSD
- Hoysond 5 in. Touch Screen Display 

​	**Misc. Components**

- (2) 1/4" Female TS Connectors
- Male RCA Connector
- 1/8" Male TRS Connector
- M3 hardware

### Assembly

1. Print out the provided case files
2. Attach the HiFiBerry hat to the Pi
3. Install the SSD and attach the NVMe base to the Pi with the provided flex cable
4. Screw the Pi into the case from below
5. Attach the screen to the Pi via  HDMI and USB
6. Screw in the lid, securing the display

Now connect the device with a USB-C power supply

## Setup and Configuration

### Preparing the OS Image

- Download the latest Patchbox OS image from the link above
- Mount the image to your device by double-clicking
- Replace config.txt with the [included file](./config.txt) or make the following changes

#### Uncomment

```bash 
dtparam=i2c_arm=on
dtparam=i2s=on
dtparam=spi=on
```

#### Comment Out

``` bash
#dtparam=audio=on
```

#### Add

```bash
dtoverlay=hifiberry-dacplusadcpro

[all]
force_eeprom_read=0
dtoverlay=w1-gpio
```

#### Edit

```bash
dtoverlay=vc4-kms-v3d -> dtoverlay=vc4-kms-v3d,noaudio
```

Unmount the edited image and flash it to an NVMe SSD using [Balena Etcher](https://balenaetcher.io) or another disk imaging tool

### Patchbox Config

**The default user is `patch` and its password is `blokaslabs`**

You can skip through the Jack settings in the Initial Setup Wizard as RAMEN relies on the ALSA audio backend

Enter the Patchbox Configuration Utility by typing `patchbox` in the terminal and make the following selections 

```
boot > environment > desktop autologin
module > none
jack > stop
kernel > install-rt
```

Install `unclutter` with `sudo apt install unclutter` and add the following to your .bashrc

```
unclutter -idle 0.01 -root
puredata path/to/repo/trem.pd
```

### ALSA Config

#### Enter the ALSA config tool by entering `alsamixer` in the terminal

- Press F6 and select `snd_rpi_hifiberry_dacplusadcpro`
- Set `ADC Left Input` to `[{VIN1p, VIN1M}[DIFF]]`
- Set `ADC Mic Bias` to `[Mic Bias Off]`

### PureData Config

#### PureData can be launched with the desktop shortcut or by typing `puredata` into a terminal window

**Under the Media tab select DSP On and ALSA then enter Audio Settings**

- Sample rate: 192000
- Delay (msec): 5
- Block size 64
- Input Devices: snd_rpi_hifiberry_dacplusadcpro (hardware)
- Output Devices: snd_rpi_hifiberry_dacplusadcpro (hardware)

Install the kiosk-plugin external through PureData's built-in external manager

Replace kiosk.cfg with the included file or set the following parameters

```

```
