import sys, datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class BlogPosts(Base):
	""" Index of blog posts """
	__tablename__ = 'blogposts'
	post_id = Column(
		Integer, primary_key = True)
	post_title = Column(
		String(80), nullable = False)

	post_content = Column(
		String(1500))

	post_group = Column(
		String(30))

	post_tags = Column(
		String(250))

	post_date = Column(
		DateTime, default=datetime.datetime.now())

engine = create_engine(
	"sqlite:///blogposts.db")

Base.metadata.create_all(engine)


