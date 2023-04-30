.phony: serve
serve:  ## Runs Hugo server locally
	hugo server -D --cacheDir /tmp
