import pandas as pd
import rpy2.robjects.packages as rpackages
from rpy2.robjects import pandas2ri, r

# Load the necessary R packages
packnames = ['tidyverse']
utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)
packnames_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
if len(packnames_to_install) > 0:
    utils.install_packages(StrVector(packnames_to_install))
    
# Activate the automatic conversion of pandas dataframes to R dataframes
pandas2ri.activate()


def genDFOfNumeratorsAndDenominatorsPython(max_denominator, min_denominator=0):
    """this generates all of the possible numberator/denominator fractions that are between 
    zero and one, given the min and max denominators
    
    Args:
        max_denominator: maximum possible denominator
        min_denominator (optional - default is 0): minimum possible denominator
        
    Returns:
        df: pandas df with all combinations of numerators and denominators
          
   """
    df = pd.DataFrame([[x, y] for x in range(0, max_denominator + 1)
                      for y in range(min_denominator, max_denominator + 1) if y >= x])
    df.columns=["Numerator", "Denominator"]
    return(df)

def genDFOfNumeratorsAndDenominatorsR(max_denominator, min_denominator=0):
    """this generates all of the possible numberator/denominator fractions that are between 
    zero and one, given the min and max denominators
    
    Args:
        max_denominator: maximum possible denominator
        min_denominator (optional - defaul is 0): minimum possible denominator
        
    Returns:
        df: pandas df with all combinations of numerators and denominators
          
   """
    rcode = """
    library(tidyverse)
    genDFOfNumeratorsAndDenominators <- function(max_denominator, min_denominator=0) {
      df <- data.frame(Numerator = integer(),
                       Denominator = integer(),
                       stringsAsFactors = FALSE)
      for (x in 0:max_denominator) {
        for (y in min_denominator:max_denominator) {
          if (y >= x) {
            df <- rbind(df, c(x, y))
          }
        }
      }
      colnames(df) <- c("Numerator", "Denominator")
      return(df)
    }
    """
    r(rcode)
    df_r = r.genDFOfNumeratorsAndDenominators(max_denominator, min_denominator)
    df = pd.DataFrame(dict(zip(df_r.names, map(list,list(df_r)))))
    return(df)

def testBothFunctions(max_denominator=10):
    dfR= genDFOfNumeratorsAndDenominatorsR(max_denominator, min_denominator=0)
    dfPython= genDFOfNumeratorsAndDenominatorsR(max_denominator, min_denominator=0)
    return(dfR.equals(dfPython))

print(testBothFunctions(max_denominator=10))