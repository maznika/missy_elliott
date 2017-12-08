# MissyElliott (Now in Python)

Credit for this idea goes to [Tom Lord's Ruby version](https://github.com/tom-lord/missy_elliott), I just felt like remaking it in Python

[![Missy Elliott](http://i.imgur.com/P23jxLq.jpg)](https://www.youtube.com/watch?v=zm28EEeyLek)

```python
MissyElliott().encode("Python") # => '0xfa0xb00xe80xf40x840xc4'

#'Python'
#--> ['P', 'y', 't', 'h', 'o', 'n']
#--> [80, 121, 116, 104, 111, 110]
#--> ['01010000', '01111001', '01110100', '01101000', '01101111', '01101110']
# Shift yo bits down
#--> ['10100000', '11110010', '11101000', '11010000', '11011110', '11011100']
# Flip it
#--> ['01011111', '00001101', '00010111', '00101111', '00100001', '00100011']
# And reverse it
#--> ['11111010', '10110000', '11101000', '11110100', '10000100', '11000100']
#--> ['0xfa', '0xb0', '0xe8', '0xf4', '0x84', '0xc4']
#--> ['0xfa0xb00xe80xf40x840xc4']

MissyElliott().decode('0xfa0xb00xe80xf40x840xc4') # => "Python"
```

This module is a blatant Python rip-off of Tom Lord's rip off of:
[an old XKCD comic](http://xkcd.com/153/):

![XKCD Comic](http://imgs.xkcd.com/comics/cryptography.png)

## Installation
$ pip install missy_elliott
