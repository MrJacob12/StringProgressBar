<p align="center">
 <a><img width=270px height=100px src="https://i.gyazo.com/eab981f7ae88b795346f6df4deca80e7.png" alt="Project logo"></a>
</p>

<h1 align="center">StringProgressBar</h1>

<div align="center">

[![GitHub Issues](https://img.shields.io/github/issues/MrJacob12/StringProgressBar.svg)](https://github.com/MrJacob12/StringProgressBar/issues)
[![License](https://img.shields.io/github/license/MrJacob12/StringProgressBar.svg)](/LICENSE)

</div>

## 📝 Table of Contents
<!-- -  -->
<!-- - [Deployment](#deployment) -->
<!-- - [Usage](#usage) -->

- [About](#about)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>
Simple string progress bar made for discord bots. Its usable everywhere.

### Advantages

* Simple
* Lightweight
* Fully customizable
* 2 Different Styles

## 🏁 Getting Started <a name = "getting_started"></a>

### Installing

A step by step series of examples that tell you how to get a development env running.

```bash
pip install StringProgressBar
```

## Splitbar Usage <a name="usage"></a>

![](https://i.ibb.co/5Yz89gM/splitbar.png)

```python
from StringProgressBar import progressBar
# Assaign values to total and current values
total = 100
current = 50
# First two arguments are mandatory
bardata = progressBar.splitBar(total, current, [optional parameters])
# Get the progressbar
print(bardata[0])
# Get the percentage
print(bardata[1])
```

## Filledbar Usage <a name="usage"></a>

![](https://i.ibb.co/ctTB8mp/filledbar.png)

```python
from StringProgressBar import progressBar
# Assaign values to total and current values
total = 100
current = 50
# First two arguments are mandatory
bardata = progressBar.filledBar(total, current, [optional parameters])
# Get the progressbar
print(bardata[0])
# Get the percentage
print(bardata[1])
```

## Optional Parameters

|Parameter name|     Type|    Default|                         Description|
|--------------|     ----|    :-----:|    --------------------------------|
|size|            Integer|         40|    Determines the length of the bar|
|line|             String|    ▬ and □|    Determines the Static part of the bar|
|slider|           String|   🔘 and ■|    Determines the Progressive part of the bar|

## ⛏️ Built Using <a name = "built_using"></a>
* [Python](https://www.python.org)

## 📝 License

This project is [MIT](https://github.com/MrJacob12/StringProgressBar/blob/master/LICENSE) licensed.


## ✍️ Authors <a name = "authors"></a>

- [@MrJacob12](https://github.com/mrjacob12)
- [@Sparker-99](https://github.com/Sparker-99)
