# Google Calendar API
## Environment
- python : ```3.8.13```
- requirements : ```pip install --upgrade -r requirements.txt```
***
## GCP setting
***
## Project Layout
```
/calendar
|---demo.py
|---Google.py
|---requirements.txt
|---token.json
|---README.md
```
***
## Quick Start
### create event
```
python demo.py --mode create \
    --calendarId primary \
    --start_time 2022,4,17,12,30 \
    --end_time 2022,4,17,14,30 \
    --event_name event_name \
    --people jimmy@gmail.com \
    --place taipei

```
- calendarId : id of calendar, default is "primary"
- start_time : start time of created event. Time format is "yyyy,mm,dd,hh,mm"
- end_time : end time of created event. Time format is "yyyy,mm,dd,hh,mm"
- event_name : the name of created event
- people : the attendee's email of this event
- place : the place of created event
  
### read event
```
python demo.py --mode read \
    --calendarId primary \
    --start_time 2022,4,17,12,30 

```
- calendarId : id of calendar, default is "primary"
- start_time : read the event start at start_time. Time format is "yyyy,mm,dd,hh,mm"

### delete event
```
python demo.py --mode delete \
    --calendarId primary \
    --start_time 2022,4,17,12,30 

```
- calendarId : id of calendar, default is "primary"
- start_time : delete the event start at start_time. Time format is "yyyy,mm,dd,hh,mm"

***
## Authentication  
When you use google calendar api at first time, you should authen your google account to let your application connect to api
### step 1
run the demo.py and select your account
<img src="./src/pic/step 1.png" />

### step 2
press continue
<img src="./src/pic/step 2.png" />

### step 3
press continue
<img src="./src/pic/step 3.png" />

### step 3
complete authentication process
<img src="./src/pic/step 4.png" />