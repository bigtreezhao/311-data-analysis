## question for Tony

## about for loop writting

yiwu202=pd.read_csv('sample.csv')

# I'm trying to create a week column in the dataset to show “week number” # 

# try 
for i in range(1001):
    test=yiwu202['OPEN_DT'][i]
    yiwu202['week'][i]=datetime.strptime(test,'%Y-%m-%d %H:%M:%S').isocalendar()[1] # not working # 

  ## similar question ##
  with open('world_dev_ind.csv') as file:

    file.readline()
    counts_dict = {}

    for j in range(0,1000):
        line = file.readline().split(',')
        first_col = line[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
   # j does not appear in loop
   
# 1 try #
for datee in yiwu202['OPEN_DT']:
    yiwu202['week']=date(datee).month   # return: an integer is required (got type Timestamp)#

# 2 try #
abc=pd.DataFrame()
for datee in yiwu202['OPEN_DT']:
    de=list(datetime.date(datee).isocalendar()[1]) # abc only contain one number #
    abc['week']=abc.append(de)

# 3 try
for datee in yiwu202['OPEN_DT']:
    yiwu202.loc['week']=datetime.strptime(datee,'%Y-%m-%d %H:%M:%S').isocalendar()[1]   
    # strptime() argument 1 must be str, not Timestamp


# try 4 #
for datee in yiwu202['OPEN_DT']:
    abc=datetime.date(datee).isocalendar()[1]
    d={'week':abc}
    yiwu202['week'].append(d) # cannot concatenate a non-NDFrame object
    
# try list comprehension # 
list = [ datetime.date(datee).isocalendar()[1] for datee in yiwu202['OPEN_DT']]
yiwu202['week']=list  # work great # 

## next pivot the data
yiwu_SUBJECT2_1=pd.read_csv('yiwu_SUBJECT2_1.csv') # for Tony
yiwu_REASON=pd.read_csv('yiwu_REASON.csv') # for Tony
yiwu_SUBJECT=pd.read_csv('yiwu_SUBJECT.csv') # for Tony


yiwu_SUBJECT2 = yiwu202.pivot_table(index='week',
                                  values='case',
                                  columns=['SUBJECT','REASON'],
                                  aggfunc='count') 
# remove na
yiwu_SUBJECT2_1=yiwu_SUBJECT2.dropna(axis='columns')

# how to generate multiple plots ? d
yiwu_SUBJECT2_1.iloc[2].plot(kind='line')

# questions:

# how to sort the total number of cases for different columns? 
# for example what are the top reasons that have most 311 cases? 

 
# test # 

