workflow "Eventex" {
  on = "push"
  resolves = "heroku.deploy" 
}

action "python.build" {
  uses = "actions/docker/cli@master"
  args = [
    "SECRET_KEY=$SECRET_KEY",
    "build -f Dockerfile -t ci-$GITHUB_SHA:latest ."
  ]
  secrets = [
    "SECRET_KEY",
  ]
}

action "python.flake8" {
  uses = "actions/docker/cli@master"
  needs = ["python.build"]
  args = "run ci-$GITHUB_SHA:latest flake8 --exclude=eventex/migrations/ eventex/"
}

action "python.test" {
  uses = "actions/docker/cli@master"
  needs = ["python.build"]
  args = "run ci-$GITHUB_SHA:latest python manage.py test eventex"
  secrets = [
    "SECRET_KEY",
  ]
}

action "git.master" {
  uses = "actions/bin/filter@master"
  needs = ["python.flake8", "python.test"]
  args = "branch master"
}

action "heroku.login" {
  uses = "actions/heroku@master"
  needs = ["git.master"]
  args = "container:login"
  secrets = ["HEROKU_API_KEY"]
}

action "heroku.push" {
  uses = "actions/heroku@master"
  needs = "heroku.login"
  args = ["container:push", "web"]
  secrets = [
    "HEROKU_API_KEY",
    "HEROKU_APP",    
  ]
}

action "heroku.envs" {
  uses = "actions/heroku@master"
  needs = "heroku.push"
  secrets = [
    "HEROKU_API_KEY",
    "HEROKU_APP",    
  ]
}

action "heroku.deploy" {
  uses = "actions/heroku@master"
  needs = ["heroku.envs", "heroku.push"]
  args = ["container:release", "web"]
  secrets = [
    "HEROKU_API_KEY",
    "HEROKU_APP",    
  ]
}