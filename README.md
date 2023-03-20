# README

This code is an example of how to use the `rpy2` library to call R code from Python and compare results between the two languages.

## Dependencies

The code requires the following Python packages to be installed:
- pandas
- rpy2

The code also requires the following R packages to be installed:
- tidyverse

## Functionality

The code contains two functions: `genDFOfNumeratorsAndDenominatorsPython` and `genDFOfNumeratorsAndDenominatorsR`.

`genDFOfNumeratorsAndDenominatorsPython` generates all possible numerator/denominator fractions between 0 and 1, given a minimum and maximum denominator. It returns a pandas dataframe.

`genDFOfNumeratorsAndDenominatorsR` is the R equivalent of `genDFOfNumeratorsAndDenominatorsPython`. It generates the same dataframe as `genDFOfNumeratorsAndDenominatorsPython`, but using R code. The R code was generated using GPT-4, and it produced the correct code on the second try. It returns a pandas dataframe.

`testBothFunctions` calls both `genDFOfNumeratorsAndDenominatorsPython` and `genDFOfNumeratorsAndDenominatorsR` with the same parameters and tests whether the resulting dataframes are the same.

## Usage

To use the code, simply import the necessary Python libraries (`pandas`, `rpy2`) and execute `testBothFunctions()`.

The code loads the `tidyverse` R package, so make sure that package is installed before running the code.

If you want to generate the dataframe using a different set of parameters, simply call `testBothFunctions(max_denominator)` with the desired maximum denominator. The default value of `max_denominator` is 10.

The output of `testBothFunctions()` will be `True` if the two dataframes are the same, and `False` otherwise.

However, as a note: this is 'False' currently even though df.compare will return an empty DataFrame - they look the same - because R is outputting the values as int32 and Python is outputting them as int64. 

Note that the purpose of this code is not the actual functionality of generating the dataframe, but rather the framework for testing whether the R and Python code produce the same results. The code allows you to call R code from Python and compare the results, all from within a Python console.
