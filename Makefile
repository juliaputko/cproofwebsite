build:
	bundler exec jekyll build

upload:
	rsync -av --delete  _site/ cproof@cproof.uvic.ca:Sites --exclude=gliderdata
