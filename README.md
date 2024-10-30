# RAMEN

## Ryan's Awesome Multi-Effects Node

RAMEN is an open music technology project created for my Music and Sound Recording Capstone for the University of New Haven. 

RAMEN relies on [Patchbox OS 2024-04-04](https://community.blokas.io/t/beta-patchbox-os-bookworm-arm64-2024-04-04/5163) and PureData Vanilla 0.53

## Build Your Own

### Componenents

- Raspberry Pi 5 8Gb
- HiFiBerry DAC2 ADC Pro
- Pimoroni NVMe Base
- NVMe SSD

​	**Misc. Components**

- (2) 1/4" TS Connectors

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

- Unmount the edited image and flash it to an NVMe SSD using [Balena Etcher](https://balenaetcher.io) or another disk imaging tool

### Patchbox Config

#### [**Note:** The default user is `patch` and its password is `blokaslabs`]

**You can skip through the Jack settings in the Initial Setup Wizard as RAMEN relies on the ALSA audio backend**

**Enter the Patchbox Configuration Utility by typing `patchbox` in the terminal and make the following selections** 

```
boot > environment > desktop autologin
module > none
jack > stop
kernel > install-rt
```

### ALSA Config

#### Enter the ALSA config tool by entering `alsamixer` in the terminal

- Press F6 and select `snd_rpi_hifiberry_dacplusadcpro`
- Set `ADC Left Input` to `[{VIN1p, VIN1M}[DIFF]]`
- Set `ADC Mic Bias` to `[Mic Bias Off]`

### PureData Config

#### PureData can be launched with the desktop shortcut or by typing `puredata` into a terminal window

**Under the Media tab select DSP On and ALSA then enter Audio Settings**

- Sample rate: 96000
- Delay (msec): 5
- Block size 64
- Input Devices: snd_rpi_hifiberry_dacplusadcpro (hardware)
- Output Devices: snd_rpi_hifiberry_dacplusadcpro (hardware)

#### [Note: All included patches are mono but RAMEN is configured to output in stereo]
