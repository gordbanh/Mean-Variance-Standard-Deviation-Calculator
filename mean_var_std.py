import numpy as np
import pandas as pd

def calculate(list):
    #test if list is 9 numbers
    try:
        #put list into array
        input = np.array(list)
        list_array=np.zeros([3,3])
        list_array[0]=input[0:3]
        list_array[1]=input[3:6]
        list_array[2]=input[6::]
        #put into pandas dataframe
        list_df=pd.DataFrame(data=list_array)
        #create calculations dataframe
        calculations=pd.DataFrame(index=['mean','variance','standard deviation','max','min','sum'],
                                 columns=['axis1','axis2','flattened'])
        #calculate mean by column
        mean_array_0=list_df.mean(axis=0)
        #calculate mean by row
        mean_array_1=list_df.mean(axis=1)
        #calculate mean by entire dataframe
        mean_array_2=list_df.mean(axis=None)
        #input into calculations dataframe
        calculations.loc['mean'] =[mean_array_0],[mean_array_1],[mean_array_2]

        #calculate variance by column
        variance_array_0=list_df.var(ddof=0,axis=0)
        #calculate variance by row
        variance_array_1=list_df.var(ddof=0,axis=1)
        #calculate variance by entire dataframe
        variance_array_2=list_df.values.var()
        #input variance into calculations dataframe
        calculations.loc['variance'] =[variance_array_0],[variance_array_1],[variance_array_2]
        
        #calculate standard deviation by column
        stdev_array_0=list_df.std(ddof=0,axis=0)
        #calculate standard deviation by row
        stdev_array_1=list_df.std(ddof=0,axis=1)
        #calculate standard deviation by entire dataframe
        stdev_array_2=list_df.values.std()
        #input standard deviation into calculations dataframe
        calculations.loc['standard deviation'] =[stdev_array_0],[stdev_array_1],[stdev_array_2]
        
        #calculate max by column
        max_array_0=list_df.max(axis=0)
        #calculate max by row
        max_array_1=list_df.max(axis=1)
        #calculate max by entire dataframe
        max_array_2=list_df.values.max()
        #input max into calculations dataframe
        calculations.loc['max'] =[max_array_0],[max_array_1],[max_array_2]

        #calculate min by column
        min_array_0=list_df.min(axis=0)
        #calculate min by row
        min_array_1=list_df.min(axis=1)
        #calculate min by entire dataframe
        min_array_2=list_df.values.min()
        #input min into calculations dataframe
        calculations.loc['min'] =[min_array_0],[min_array_1],[min_array_2]

        #calculate sum by column
        sum_array_0=list_df.sum(axis=0)
        #calculate sum by row
        sum_array_1=list_df.sum(axis=1)
        #calculate sum by entire dataframe
        sum_array_2=list_df.values.sum()
        #input sum into calculations dataframe
        calculations.loc['sum'] =[sum_array_0],[sum_array_1],[sum_array_2]

        print(calculations.dtypes)
        
    except ValueError:
        raise ValueError("List must contain nine numbers")

    return calculations