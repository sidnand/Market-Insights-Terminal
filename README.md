# Financial Data Terminal

## Usage

Currently supports USA stocks and economy data. Canada will be added soon.

1. Create a `config.json` file with:

```json
{
    "api_key": {
      "fred": ""
    },
    
    "user": {
      "name": "",
      "email": ""
    }
  }
```

2. Run the following commands to get the data:

```bash

python main.py search --category ticker --country usa <ticker>
python main.py search --category economy --country usa <query search>

python main.py download --category ticker --country usa <ticker> --annual
python main.py download --category ticker --country usa <ticker> --quarterly
python main.py download --category ticker --country usa <ticker> --stock

python main.py download --category economy --country usa <FRED ID>

```
