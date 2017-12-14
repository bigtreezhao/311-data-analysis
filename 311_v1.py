import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date, time
plt.style.use('ggplot') # Look Pretty

yiwu_2 =pd.read_csv('311__2015-2016.csv')

yiwu =pd.read_csv('311__2015-2016.csv', index_col='OPEN_DT', parse_dates=True)

yiwu2=yiwu.drop(['CASE_ENQUIRY_ID', 'TARGET_DT', 'CLOSED_DT',
       'CASE_STATUS', 'CLOSURE_REASON', 'CASE_TITLE', 'QUEUE', 'Department', 
       'SubmittedPhoto', 'ClosedPhoto',
       'Location', 'fire_district', 'pwd_district', 'city_council_district',
       'police_district','ward', 'precinct', 'land_usage', 'LOCATION_STREET_NAME',
       'Property_Type', 'Property_ID', 'LATITUDE',
       'LONGITUDE', 'Geocoded_Location'],axis=1)

yiwu2=yiwu2.sort_index(ascending=True)
yiwu201=yiwu2.reset_index()
yiwu202=yiwu201.reset_index()

#  list comprehension get week number# 
list = [ datetime.date(datee).isocalendar()[1] for datee in yiwu202['OPEN_DT']]
yiwu202['week']=list  # work great # 

#pandas datatime get week number#
yiwu202['OPEN_DT2']=pd.to_datetime(yiwu202['OPEN_DT'])

yiwu202['OPEN_DT2'].dt.day
yiwu202['OPEN_DT2'].dt.weekday
.dt.dayofyear
.dt.month
.dt.week

yiwu202['week']=pd.to_datetime(yiwu202['OPEN_DT']).dt.week

# pivot table #
yiwu202['case']=1

yiwu_SUBJECT = yiwu202.pivot_table(index='week',
                                  values='case',
                                  columns='SUBJECT',
                                  aggfunc='count') 
yiwu_REASON = yiwu202.pivot_table(index='week',
                                  values='case',
                                  columns='REASON',
                                  aggfunc='count') 

yiwu_SUBJECT2 = yiwu202.pivot_table(index='week',
                                  values='case',
                                  columns=['SUBJECT','REASON'],
                                  aggfunc='count') 

yiwu_SOURCE = yiwu202.pivot_table(index='week',
                                  values='case',
                                  columns=['Source'],
                                  aggfunc='count')
                                 
yiwu_neighbor = yiwu202.pivot_table(index='week',
                                  values='case',
                                  columns=['neighborhood'],
                                  aggfunc='count')
(,margins=True) 

yiwu_SUBJECT.to_csv('yiwu_SUBJECT.csv')
yiwu_REASON.to_csv('yiwu_REASON.csv')
yiwu_SUBJECT2.to_csv('yiwu_SUBJECT2.csv')
yiwu_REASON.to_csv('yiwu_SOURCE.csv')


# remove na
yiwu_SUBJECT2_1=yiwu_SUBJECT2.dropna(axis='columns')

# use .unstack to get the mean, standard deviation (std) ##  
yiwu202['SUBJECT'].describe().unstack


## 311 calling source graph results 

# all time plot

yiwu_SOURCE.plot(x=yiwu_SOURCE.index,y=['Citizens Connect App', 'City Worker App',
       'Constituent Call', 'Employee Generated','Self Service'], kind='line',figsize=(8, 8))
# plot exclude first 9 weeks
yiwu_SOURCE.iloc[9:-1].plot(x=yiwu_SOURCE.iloc[9:-1].index,y=['Citizens Connect App', 'City Worker App',
       'Constituent Call', 'Employee Generated','Self Service'], kind='line',figsize=(8, 8))

# area plot
yiwu_SOURCE.iloc[:-1].plot(x='week',y=['Citizens Connect App', 'City Worker App',
       'Constituent Call', 'Employee Generated','Self Service'], kind='area')
yiwu_SOURCE.iloc[9:-1].plot(x='week',y=['Citizens Connect App', 'City Worker App',
       'Constituent Call', 'Employee Generated','Self Service'], kind='area')

# pie plot
source_total=yiwu_SOURCE.sum(axis=0)
source_total[:4].plot.pie(figsize=(8, 8))

## 311 calling subject graph results 
subject_total=yiwu_SUBJECT.sum(axis=0).sort_values(ascending=True)

subject_total.reset_index().plot(kind='bar',x='SUBJECT',y=0,figsize=(8, 8))

# select some column
pub_work=yiwu_SUBJECT.columns[-4]
Trans_Inspec=yiwu_SUBJECT.columns[[-3,-9]]
yiwu_SUBJECT.plot(x=yiwu_SUBJECT.index,y=pub_work, kind='bar',figsize=(8, 8))
yiwu_SUBJECT.plot(x=yiwu_SUBJECT.index,y=Trans_Inspec, kind='bar',figsize=(18, 8))
yiwu_SUBJECT.plot(x=yiwu_SUBJECT.index,y=['Animal Control', 'Boston Police Department',
       'Boston Water & Sewer Commission', 'City Hall Truck', 'Civil Rights',
       'Disability Department',
       "Mayor's 24 Hour Hotline", 'Neighborhood Services',
       'Parks & Recreation Department', 'Property Management',
               'Veterans', 'Youthline'], kind='line',figsize=(18, 10))

## 311 calling reason graph results  
reason_total=yiwu_REASON.sum(axis=0)
reason_total=reason_total.sort_values(ascending=True)
yiwu_REASON.plot(kind='bar',use_index=True,figsize=(20, 10))


yiwu_REASON.plot(use_index=True,y=reason_total.index[-1], kind='line',figsize=(8, 8))

yiwu_REASON.plot(use_index=True,y=reason_total.index[-3:-1], kind='line',figsize=(8, 8))

yiwu_REASON.plot(use_index=True,y=reason_total.index[-8:-3], kind='bar',figsize=(8, 8))
yiwu_REASON.plot(use_index=True,y=reason_total.index[-8:-3], kind='area',figsize=(15, 8))
yiwu_REASON.plot(use_index=True,y=reason_total.index[-15:-8], kind='line',figsize=(15, 8))
yiwu_REASON.plot(use_index=True,y=reason_total.index[-20:-15], kind='line',figsize=(8, 8))

## 311 calling neighborhoods graph results  

neighbor_total=yiwu_neighbor.sum(axis=0)
neighbor_total=neighbor_total.sort_values(ascending=True)
neighbor_total.plot(kind='bar',use_index=True,figsize=(15, 10))


yiwu_neighbor.plot(use_index=True,y=neighbor_total.index[-1], kind='line',figsize=(8, 8))

yiwu_neighbor.plot(use_index=True,y=neighbor_total.index[-6:], kind='line',figsize=(8, 8))

yiwu_neighbor.plot(use_index=True,y=neighbor_total.index[-11:-6], kind='line',figsize=(8, 8))
yiwu_neighbor.plot(use_index=True,y=neighbor_total.index[-8:-3], kind='area',figsize=(15, 8))
y

## 311 calling subject+reason graph

sub_rea_total=yiwu_SUBJECT2.sum(axis=0)
sub_rea_total=sub_rea_total.sort_values(ascending=True)
sub_rea_total.plot(kind='bar',use_index=True,figsize=(15, 10))

yiwu_SUBJECT2.plot(use_index=True,y=sub_rea_total.index[-1], kind='line',figsize=(8, 8))

yiwu_SUBJECT2.plot(use_index=True,y=sub_rea_total.index[-6:-1], kind='line',figsize=(14, 8))

yiwu_SUBJECT2.plot(use_index=True,y=sub_rea_total.index[:-16], kind='area',figsize=(20, 10))
yiwu_SUBJECT2.plot(use_index=True,y=sub_rea_total.index[-8:-6], kind='line',figsize=(10, 6))

# plot exclude first 9 weeks
yiwu_SUBJECT.iloc[9:-1].plot(x=yiwu_SUBJECT.iloc[9:-1].index,y=['Citizens Connect App', 'City Worker App',
       'Constituent Call', 'Employee Generated','Self Service'], kind='line',figsize=(8, 8))



yiwu202.week.value_counts('case').sort_index().plot() # total case number # 

plt.plot(yiwu_SOURCE, yiwu_SOURCE.iloc[4])
yiwu_SOURCE.iloc[0].plot.line().gcf().autofmt_xdate()
yiwu_SOURCE.iloc[0].plot.line().gcf().autofmt_xdate()
yiwu_SOURCE=yiwu_SOURCE.reset_index()

plt.plot(yiwu_SOURCE[:-1]['week'],yiwu_SOURCE[:-1]['Citizens Connect App'])

plt.subplot=(2,2,1)
yiwu_SOURCE.iloc[9:-1].plot(x='week',y=['Citizens Connect App', 'City Worker App',
       'Constituent Call', 'Employee Generated', 'Maximo Integration',
       'Self Service', 'Twitter'], kind='line')

yiwu_SOURCE.iloc[-1,2:6:].plot( kind='pie')

plt.subplot=(2,2,2)
yiwu_SOURCE.iloc[:-1].plot(x='week',y='City Worker App', kind='line')

plt.subplot=(2,2,3)
yiwu_SOURCE.iloc[:-1].plot(x='week',y='Constituent Call', kind='line')

plt.subplot=(2,2,4)
yiwu_SOURCE.iloc[:-1].plot(x='week',y='Employee Generated', kind='line')

from pandas.plotting import andrews_curves
plt.figure()
andrews_curves(yiwu_SOURCE, yiwu_SOURCE.columns[2:])


yiwu_SUBJECT2_1.iloc[3].plot()
plt.xlable('')

subject2_index=yiwu_SUBJECT2_1.columns
for idx, val in enumerate(enumerate(subject2_index)):
    yiwu_SUBJECT2_1.iloc[idx].plot(kind='line')

## 


