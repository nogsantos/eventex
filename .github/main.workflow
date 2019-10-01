workflow "Eventex" {
  on = "push"
  resolves = "heroku.deploy"
}

action "python.build" {  
  args = "build -f Dockerfile -t ci-$GITHUB_SHA:latest ."
}

action "python.flake8" {
  uses = "ci-$GITHUB_SHA:latest"
  needs = ["python.build"]
  args = "run ci-$GITHUB_SHA:latest flake8 --exclude=eventex/migrations/ eventex/"
}

action "python.test" {
  uses = "ci-$GITHUB_SHA:latest"
  needs = ["python.build"]
  args = "run ci-$GITHUB_SHA:latest python ./manage.py test"
  secrets = [
    "SECRET_KEY",
  ]
  env = {
    ALLOWED_HOSTS = "0.0.0.0"
    DJANGO_SETTINGS_MODULE = "eventex.settings"
  }
}

action "git.master" {
  uses = "ci-$GITHUB_SHA:latest"
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
  env = {
    ALLOWED_HOSTS = "0.0.0.0"
  }
}

action "heroku.envs" {
  uses = "actions/heroku@master"
  needs = "heroku.push"
  secrets = [
    "HEROKU_API_KEY",
    "HEROKU_APP",
    "SECRET_KEY",
  ]
}

action "heroku.deploy" {
  uses = "actions/heroku@master"
  needs = ["heroku.envs", "heroku.push"]
  args = ["container:release", "web"]
  secrets = [
    "HEROKU_API_KEY",
    "HEROKU_APP",
    "SECRET_KEY",
  ]
}
