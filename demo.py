from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime
from argparse import ArgumentParser, Namespace

def main(args):
    # api parameter
    CLIENT_SECRET_FILE = "token.json"
    API_NAME = "calendar"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    # create api service
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # load calendar ID
    calendarId = args.calendarId

    # load start time of event
    start_time = args.start_time.split(",")
    assert(len(start_time) == 5)
    s_year = int(start_time[0])
    s_month = int(start_time[1])
    s_day = int(start_time[2])
    s_hour = int(start_time[3])
    s_minute = int(start_time[4])

    # load end time of event
    end_time = args.end_time.split(",")
    assert(len(end_time) == 5)
    e_year = int(end_time[0])
    e_month = int(end_time[1])
    e_day = int(end_time[2])
    e_hour = int(end_time[3])
    e_minute = int(end_time[4])

    # adjust rfc3339 time to local time
    hour_adjust = -8

    # create event given name, place, start time, end time , attendees
    if args.mode == "create":
        event_request_body = {
            "summary" : args.event_name,
            "location" : args.place,
            "start": {
                "dateTime": convert_to_RFC_datetime(s_year, s_month, s_day, s_hour + hour_adjust, s_minute),
                "timeZone": "Asia/Taipei",
            },
            "end": {
                "dateTime": convert_to_RFC_datetime(e_year, e_month, e_day, e_hour + hour_adjust, e_minute),
                "timeZone": "Asia/Taipei",
            },
            "attendees": [
                {"email": args.people},
            ],
        }
        event = service.events().insert(calendarId=calendarId, body=event_request_body).execute()

    # read event occur at start time day(yyyy-mm-dd)
    elif args.mode == "read":
        event = service.events().list(calendarId=args.calendarId).execute()
        for i in event["items"]:
            if "date" in i["start"].keys():
                if i["start"]["date"] == convert_to_RFC_datetime(s_year, s_month, s_day, s_hour + hour_adjust, s_minute)[:10]:
                    pprint(i)

            if "dateTime" in i["start"].keys():
                if i["start"]["dateTime"][:10] == convert_to_RFC_datetime(s_year, s_month, s_day, s_hour + hour_adjust, s_minute)[:10]:
                    pprint(i)      
                          
    # delete event occur at start time day(yyyy-mm-dd)
    elif args.mode == "delete":
        event = service.events().list(calendarId=args.calendarId).execute()
        for i in event["items"]:
            if "date" in i["start"].keys():
                if i["start"]["date"] == convert_to_RFC_datetime(s_year, s_month, s_day, s_hour + hour_adjust, s_minute)[:10]:
                    service.events().delete(calendarId=args.calendarId, eventId=i["id"]).execute()

            if "dateTime" in i["start"].keys():
                if i["start"]["dateTime"][:10] == convert_to_RFC_datetime(s_year, s_month, s_day, s_hour + hour_adjust, s_minute)[:10]:
                    service.events().delete(calendarId=args.calendarId, eventId=i["id"]).execute()
                     

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "--calendarId", type=str, help="calendar Id.", default="primary"
    )
    parser.add_argument(
        "--mode", type=str, help="calendar mode.", required=True
    )
    parser.add_argument(
        "--start_time", type=str, help="calendar time.", default="2022,4,17,12,30"
    )
    parser.add_argument(
        "--end_time", type=str, help="calendar time.", default="2022,4,17,12,30"
    )
    parser.add_argument(
        "--event_name", type=str, help="calendar event.", default="test"
    )
    parser.add_argument(
        "--people", type=str, help="calendar attendee people email.", default="jimmy@gmail.com"
    )
    parser.add_argument(
        "--place", type=str, help="calendar place.", default="taiwan"
    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)