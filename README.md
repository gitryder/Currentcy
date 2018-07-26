# Currentcy
A Python Module that crawls the web for current currency rates and returns them for ease of access

## Usage
```
import currentcy as crate

rate = crate.currentcy_rate(FROM, TO, multiplier)
```
*The `multiplier` default is 1* 

Eg.
```
currentcy_rate("USD", "AUD", 35)
```
> returns 35 USD converted to AUD

## Currency Codes 
You can find the most common currency codes [here](https://gist.github.com/gitryder/9b550eac061cb6c1980c1573ec011817)
