# Currentcy
A Python Module that crawls the web for current currency rates and returns them for ease of access

## Usage
```
import currentcy as crate

rate = crate.currentcy_rate(FROM, TO, multiplier)
```
*The `multiplier` default is 1* 

You can find almost all currency codes [here](https://gist.github.com/gitryder/9b550eac061cb6c1980c1573ec011817)

Eg.
```
currentcy_rate("USD", "AUD", 35)
```
