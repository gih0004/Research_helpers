# Research_helpers
This repository is to store different scripts that can be implemented for automating different experimental setups

## Chem_Calc.py ##

If you're as profficient as me when calculating stock solutions, you might find this stock solution calculator of use. 

📋 Required Data: Chemicals of interest and their molecular weight[g/mol] 

📊 Example Data: To get a glimpse of this code, download the Molwght.csv file

Here I'll give an overview of the code:

### Step 1. Define Chemicals and of interest in a csv file ###


|     Chemical     | Molecular Weight |
|------------------|------------------|
| BA               | 225.3            |
| IBA              | 203.2            |



> [!TIP]
> I recomend having a csv file where you periodically update any chemicals you may use and that way the script will always be up to date


### Step 2. Run application ###
```
pip install streamlit #install streamlit if first time
```
To run the script, open the terminal or terminal emulator and run :
```
streamlit run Chem_Calc.py 
```

### Step 3. Application Input ###

The application should load momentarily 

The required input is : 
- Path to CSV file: can be a whole path or the file name if script is in the same directory
- Amount of chemicals to include in your solution: numeric value
- Chemical: Toggle down menu based on the dictionary keys that are created from the chemicals column in the csv file
- Unit of Volume [microLiter, MilliLiter, or Liter]: case insensative but most have correct spelling 
- Unut of Molarity [microMolar, MilliMolar, or Molar]: case insensative but most have correct spelling 
- Desired final concentration for the chemical in the solution : numeric value corresponding to unit of molarity

### Step 4. Media Recipe ###

After entering the required input, the amount of grams, miligrams or micrigrams (denoted based of quanitity required) will be printed in the terminal along with a summary table of the chemicals. 

|     Chemical     | Amount     |    Unit     |
|------------------|------------|-------------|
| BA               | 225.3      | micrograms  |
| IBA              | 3.2        |     grams   |


