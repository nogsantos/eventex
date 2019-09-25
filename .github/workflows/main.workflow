workflow "Deploy to Heroku" {
  on = "push"
  resolves = "release"
}

action "login" {
  uses = "actions/heroku@master"
  args = "container:login"
  secrets = ["HEROKU_API_KEY"]
}

action "push" {
  uses = "actions/heroku@master"
  needs = "login"
  args = "container:push -a eventex-nogsantos web"
  secrets = ["HEROKU_API_KEY"]
}

action "release" {
  uses = "action/heroku@master"
  needs = "push"
  args = "container:release -a eventex-nogsantos web"
  secrets = ["HEROKU_API_KEY"]
}