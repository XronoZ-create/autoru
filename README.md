# AutoruParser
Парсер обьявлений на [Autoru](https://auto.ru)


# Стек

 - Python 3.9
 - BeautifoulSoup
 - Selenium-wire

## Quick Start

`git clone https://github.com/XronoZ-create/autoru.git`
```
from autoru import total_count, marks, mark_models
a = total_count(proxy='your_proxy', headless=False)
a = mark_models(proxy='your_proxy', headless=False, mark_model_url='https://auto.ru/moskva/cars/ac/all/')
```
