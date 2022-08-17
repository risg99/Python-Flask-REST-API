# Importing necessary libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# Initialising Flask APP and API
app = Flask(__name__)
api = Api(app)

# Instantiate request parser for put API
video_put_args = reqparse.RequestParser()		

# Adding required arguments for a video object type -> name, likes and views
video_put_args.add_argument("videoName",type=str,help="Name of the video is required",required=True)
video_put_args.add_argument("videoViews",type=int,help="Views of the video is required",required=True)
video_put_args.add_argument("videoLikes",type=int,help="Likes on the video is required",required=True)

# Creating a videos object
videos = {}

# Creating abort functions when video_id exists or not exists
def abort_if_video_doesnt_exists(video_id):
	if video_id not in videos:
		abort(404, message = "Video doesn't exist against this id...")

def abort_if_video_exists(video_id):
	if video_id in videos:
		abort(409, message = "Video already exists against this id...")

# Adding Resources
class Video(Resource):

	# Handling get requests
	def get(self,video_id):
		abort_if_video_doesnt_exists(video_id)
		return videos[video_id]

	# Handling put requests
	def put(self,video_id):
		abort_if_video_exists(video_id)
		videoArgs = video_put_args.parse_args()
		videos[video_id] = videoArgs
		return videos[video_id], 201		

	def delete(self,video_id):
		abort_if_video_doesnt_exists(video_id)
		del videos[video_id]
		return '', 204

# Registering the resource with api
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
	# running Flask server
	app.run(debug=True)		