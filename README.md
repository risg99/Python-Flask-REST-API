# Python-Flask-REST-API
This is a sample YouTube API demonstrating the usage of Python Flask APIs.

Functions accomplished:
1) Get Video
- fetches video from object/DB using the video_id when passed as a parameter
- if a video doesn't exist, an error message is returned
- response is a video along with it's arguments of id, name, likes, views

2) Put Video
- using the argument values, video object is appended with new data
- if a video already exists, an error message is returned
- response is a video along with it's arguments of id, name, likes, views
- a customised status code of 201 is also returned to server, depicting Successful data creation

3) Patch Video
- fetches video from object/DB using the video_id when passed as a parameter
- using the new argument values, video object is stored with new data
- if a video doesn't exists, an error message is returned
- response is a video along with it's arguments of id, name, likes, views

4) Delete Video
- fetches video from object/DB using the video_id when passed as a parameter and deleted
- if a video doesn't exist, an error message is returned
- response is a null value 
- a customised status code of 204 is also returned to server, depicting Successful data deletion


Some API Statuses used in this application:-
- 200 - OK
- 201 - Created
- 204 - Deleted successfully
- 404 - Page not found
- 409 - Already exists

A few notable points:
- Whenever trying to return from REST APIs' functions, it should be JSON Serializable
- Arguments are passed to APIs within <> with variable type and name
- Installing the dependencies: pip install -r requirements.txt
