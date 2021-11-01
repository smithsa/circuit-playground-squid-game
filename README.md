# Circuit Playground Squid Game
"Red Light, Green Light" game, inspired by "Squid Game". 

The project was built using the Circuit Playground Express and coded in Micropython. The code utilizes the Circuit Playground Express' built-in triple-axis accelerometer, magnetic speaker/buzzer, push button, and LEDs. 

:warning: Game uses a gun shot to indicate a player has lost.

# Prerequisites

- [Ciruit Playground Express](https://www.adafruit.com/product/3333)
- [CircuitPython](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart)

N.B. your devise will need at least 1MB of space, not including libraries and utilities.

# Installation

1. Clone the repository

```
git clone https://github.com/smithsa/circuit-playground-squid-game.git
```

2. Connect you Circuit Playground Express to your computer and you should see a "CIRCUITPY" disk drive

4. Load the content of the repository onto the "CIRCUITPY" disk drive

5. If you need to connect to a serial port be sure to checkout Adafruit's ["Conencting to the Serial Port"](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console) tutorial

# Usage

Simple to use, basic "Red Light, Green Light Game." When the light is green and the audio indicate so, you are free to move. When the light is no longer green, you must stop otherwise you lose the game. Enjoy!
