### continue from 311_v1.py


yiwu3=yiwu.drop(['CASE_ENQUIRY_ID','CLOSURE_REASON', 'CASE_TITLE', 'QUEUE', 'Department', 
       'SubmittedPhoto', 'ClosedPhoto','Location', 'fire_district',
       'pwd_district', 'city_council_district',
       'police_district','ward', 'precinct', 'land_usage', 'LOCATION_STREET_NAME',
       'Property_Type', 'Property_ID', 'Geocoded_Location'],axis=1)

yiwu3=yiwu3.sort_index(ascending=True)
yiwu301=yiwu3.reset_index()
)

## calculate duration 
yiwu301['OPEN_DT']=pd.to_datetime(yiwu301['OPEN_DT'])
yiwu301['CLOSED_DT']=pd.to_datetime(yiwu301['CLOSED_DT'])
yiwu301['Duration']=yiwu301['CLOSED_DT']-yiwu301['OPEN_DT']

yiwu301['SOLVE_DAY']=yiwu301['Duration'].dt.days
yiwu301['SOLVE_HOUR']=yiwu301['Duration'].dt.hour ## why no attribute 'hour'?

# plot histogram of case solve duration
yiwu301['SOLVE_DAY'].plot.hist()
yiwu301[yiwu301['SOLVE_DAY']<=8]['SOLVE_DAY'].plot.hist()


### calculate late cases
iwu302=yiwu301.drop(['CASE_STATUS','neighborhood_services_district'],axis=1) 
yiwu302=yiwu302.dropna()
yiwu302.describe() # dataset with target closing date # 

yiwu302['CLOSED_DT']=pd.to_datetime(yiwu302['CLOSED_DT'])
yiwu302['TARGET_DT']=pd.to_datetime(yiwu302['TARGET_DT'])
yiwu302['LATE']=yiwu302['CLOSED_DT']>yiwu302['TARGET_DT']

yiwu302['LATE'].describe()
yiwu302.to_csv('yiwu302.csv')

# check whether the generated "late" equals to 'Ontime_Status'
delay_case=yiwu302.groupby("LATE").agg([len]) # same thing
delay_case2=yiwu302.groupby("OnTime_Status").count() # self created LATE equals to ontime status


## NA cases analysis ## --yiwu303--all na cases of target_dt
yiwu303=yiwu301[yiwu301['TARGET_DT'].isnull()] 
# set categorical to subject and reason
yiwu303['SUBJECT']=yiwu303[['SUBJECT'].astype('category')
,'REASON', 'TYPE', 'neighborhood','Source']
yiwu301.
# use groupby to see what kind of cases do not have target date
na_case=yiwu303.groupby(['SUBJECT','REASON']).count()
na_case.to_csv('nacase.csv')
na_case2=yiwu303.groupby(['SUBJECT','REASON','TYPE']).count()
na_case2.to_csv('nacase2.csv')

na_case_table=yiwu301.groupby(['OnTime_Status']).count()
na_case_table_2=yiwu301.groupby("OnTime_Status").agg([len]) # same thing

### 311 ontime analysis ## 
yiwu304_ontime=yiwu302[yiwu302['OnTime_Status']=='ONTIME'] 
yiwu304_overdue=yiwu302[yiwu302['OnTime_Status']=='OVERDUE'] 

## ontime cases
ontime_case=yiwu304_ontime.groupby(['SUBJECT','REASON']).count()
ontime_case.to_csv('ontime_case.csv')
ontime_case2=yiwu304_ontime.groupby(['SUBJECT','REASON','TYPE']).count()
ontime_case2.to_csv('ontime_case2.csv')
ontime_case2=ontime_case2.reset_index()
ontime_case2=ontime_case2.sort_values(by='CLOSED_DT',ascending=False)
ontime_case2.iloc[:20,:].plot(x=['REASON','TYPE'],y=['OPEN_DT'],kind='bar',figsize=(10,8))

ontime_case2.head()

## overdue cases
over_case=yiwu304_overdue.groupby(['SUBJECT','REASON']).count()
over_case.to_csv('over_case.csv')
over_case2=yiwu304_overdue.groupby(['SUBJECT','REASON','TYPE']).count()
over_case2.to_csv('over_case2.csv')

over_case2=over_case2.reset_index()
over_case2=over_case2.sort_values(by='CLOSED_DT',ascending=False)
over_case2.iloc[1:20,:].plot(x=['REASON','TYPE'],y=['OPEN_DT'],kind='bar',figsize=(10,8))

over_case2.loc['Public Works Department','Street Cleaning']

over_case2.plot(use_index=True,y='OPEN_DT', kind='bar',figsize=(15, 8))
