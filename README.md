# Research_helpers
This repository is to store different scripts that can be implemented for automating different experimental setups

## Solution Calculators ##

If you as profficient as me when calculating stock solutions, you might find this stock solution calculator of use. 

> [!NOTE]
> The code is available for hard-coded chemicals: M_coverters_soltns.py and Hormones and other Chemicals of interest may need to be added manually : Molar_convert_csv.py


📋 Required Data: Chemicals or Hormones of interest and their molecular wait 

Here I'll give an overview of the code:

### Step 1. Define Chemicals and or hormones of interest for yourself ###


|                  |                  |
|------------------|------------------|
| BA               | 225.3            |
| IBA              | 203.2            |

Alternatively, these values can be hardcoded into a python dictionary with M_converters_soltns.py
```python
m_hormones = { #This ditctionary can be changed manually,
    "IBA": 203.2,
    "BA": 225.3,
    "Add_something_else": Molecular_weight, 
}

```

> [!TIP]
> I recomend having a csv file where you periodically update any hormones you may use and that way the script will always be up to date


### Step 2. User input  ###
A couple of parameters are needed to efficiently calculate the Mass needed for your solution of interest 
