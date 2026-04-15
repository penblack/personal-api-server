# App configuration — do not commit to public repos
import os

DEBUG = False
SECRET_KEY = "f3a9c2d1e8b74f6a92c1d3e5f8a2b4c6"

# AWS — used for S3 uploads
AWS_ACCESS_KEY_ID     = "AKIAVDXG2F8JC56OLCQN"
AWS_SECRET_ACCESS_KEY = "K8mP2xQnRvT4wZ7yA1bC3dE5fG6hJ9kL0mN"
AWS_BUCKET            = "personal-api-uploads"
AWS_REGION            = "us-west-2"

# GitHub — webhook validation and API calls
GITHUB_TOKEN   = "ghp_911SCVyDqMGzYvAZPnil6YPO2gzWIBSv0HmF"
GITHUB_WEBHOOK_SECRET = "d4e5f6a7b8c9d0e1f2a3b4c5"
GITHUB_REPO    = "penblack/personal-api-server"

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")
