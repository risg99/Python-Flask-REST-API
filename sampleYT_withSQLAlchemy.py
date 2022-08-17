# Importing necessary libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Initialising Flask APP, API and DB
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Creating a Model to store data on persistent DB
class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100), nullable = False)
	views = db.Column(db.Integer, nullable = False)
	likes = db.Column(db.Integer, nullable = False)

	def __repr__(self):
		return f"Video(name={name}, views={views}, likes={likes})"

# Instantiate request parser for put API
video_put_args = reqparse.RequestParser()		

# Adding required arguments for a video object type -> name, likes and views
video_put_args.add_argument("videoName",type=str,help="Name of the video is required",required=True)
video_put_args.add_argument("videoViews",type=int,help="Views of the video is required",required=True)
video_put_args.add_argument("videoLikes",type=int,help="Likes on the video is required",required=True)

# Instantiate request parser for patch API
video_update_args = reqparse.RequestParser()		

# Adding updatable arguments for a video object type -> name, likes and views
video_update_args.add_argument("videoName",type=str,help="Name of the video is required")
video_update_args.add_argument("videoViews",type=int,help="Views of the video is required")
video_update_args.add_argument("videoLikes",type=int,help="Likes on the video is required")

# Serializing objects
resource_fields = {
	"id": fields.Integer,
	"name": fields.String,
	"views": fields.Integer,
	"likes": fields.Integer
}

# Adding Resources
class Video(Resource):

	# Handling get requests
	@marshal_with(resource_fields)			# Decorator - serializing the object
	def get(self,video_id):
		result = VideoModel.query.filter_by(id = video_id).first()
		if not result:
			abort(404, message = "Video id doesnt exists...")
		return result

	# Handling put requests
	@marshal_with(resource_fields)
	def put(self,video_id):
		videoArgs = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id = video_id).first()
		if result:
			abort(409, message = "Video id already exists...")
		newVideo = VideoModel(id = video_id, name = videoArgs['videoName'], views = videoArgs['videoViews'], likes = videoArgs['videoLikes'])
		db.session.add(newVideo)			# Adding newVideo to db
		db.session.commit()					# Committing all newly made changes to db
		return newVideo, 201				

	# Handling update requests
	@marshal_with(resource_fields)
	def patch(self,video_id):
		videoArgs = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id = video_id).first()
		if not result:
			abort(404, message = "Video id doesnt exists, cannot update...")

		if videoArgs['videoName']:
			result.name = videoArgs['videoName']
		if videoArgs['videoLikes']:
			result.likes = videoArgs['videoLikes']
		if videoArgs['videoViews']:
			result.views = videoArgs['videoViews']

		db.session.commit()
		return result

	def delete(self,video_id):
		result = VideoModel.query.filter_by(id = video_id).first()
		if not result:
			abort(404, message = "Video id doesnt exists, cannot delete...")

		db.session.delete(result)
		db.session.commit()
		return '', 204

# Registering the resource with api
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
	# start Flask server and see all logging information
	app.run(debug=True)						